from src.pkg.interfaces.externalInterfaces import RobotExternalInterface
# from managedThread import ManagedThread
import URBasic
import time


class mitsubishConn(RobotExternalInterface):
    """
    Classe de comunicação com o UR5e. Essa classe implemneta a interface RobotExternalInterface,
    que define os métodos que a arquitetura irá utilizar para a comunicação com o robô.
    
    A classe Ur5eComm utiliza a biblioteca URBasic (hope robotics), que é uma biblioteca de comunicação com robôs UR.
    
    Args:
        robotIp (str): IP do robô
        robotPort (int, optional): Porta do robô. Defaults to 30004.
        robotSpeed (float, optional): Velocidade do robô. Defaults to 0.1.
    
    Methods:
        connectToRobot(): Conecta com o robô
        disconnectFromRobot(): Desconecta do robô
        getTcpPositionFromRobot(): Retorna a posição do TCP do robô
        getTcpForceFromRobot(): Retorna a força do TCP do robô
        sendPositionToRobot(pose: list, positionType: int): Envia uma posição para o robô
        runCodeOnRobot(): Executa um código no robô
        stopCodeOnRobot(): Para a execução de um código no robô
    """
    
    
    def __init__(self, robotIp:  str, 
                       robotPort: int = 30004,
                       robotSpeed: float = 0.1,):
        
        """
            Conexão com o robô fisico.
            
            Args:
                robotIp (str): IP do robô
                robotPort (int, optional): Porta do robô. Defaults to 30004.
                robotSpeed (float, optional): Velocidade do robô. Defaults to 0.1.
        """
        self._robotModel = URBasic.robotModel.RobotModel()
        self._robotIp = robotIp
        self._robot = None
        self._robotSpeed = robotSpeed
    
    def connectToRobot(self) -> bool:
        """
        Conecta com o robô (Implementação da interface)
        
        Returns: 
            bool: True se conectou, False se não conectou
        """
        # Implement this method to connect to the robot
        self._robot = URBasic.urScriptExt.UrScriptExt(host=self._robotIp,robotModel=self._robotModel)
        return True
    
    def disconnectFromRobot(self) -> bool:
        """
        Desconecta do robô (Implementação da interface)
        
        Returns:
            bool: True se desconectou, False se não desconectou
        """
        # Implement this method to disconnect from the robot
        if self._robot is not None:
            self._robot.close()
            return True
        else:
            # raise Exception("O robô não existe na classe de integração externa. -> " + str(self))
            return False
        
    
    def getTcpPositionFromRobot(self) -> list:
        """
        Pega posição do TCP atual do robô (Implementação da interface)
        
        returns:
            list: Posição do TCP do robô : [x, y, z, rx, ry, rz]
        """
        # Implement this method to get TCP position from the robot
        if self._robot:
            actualPos = self._robot.get_actual_tcp_pose()
            return actualPos
        else:
            raise Exception("O robô não existe na classe de integração externa. -> " + str(self))
    
    def getTcpForceFromRobot(self) -> list:
        """
        Pega força do TCP atual do robô (Implementação da interface)
        
        returns:
            list: Força do TCP do robô : [fx, fy, fz, tx, ty, tz]
        """
        # Implement this method to get TCP force from the robot
        if self._robot:
            # actualForce = self._robot.get_actual_tcp_force() #Não implementado na biblioteca utilizada
            actualTcpForce = self._robot.robotConnector.RobotModel.dataDir["actual_TCP_force"]
            return actualTcpForce
        else:
            # return False
            raise Exception("O robô não existe na classe de integração externa. -> " + str(self))
    
    def sendPositionToRobot(self, pose: list, positionType: int) -> bool:
        """
        Envia posição para o robô (Implementação da interface)
        
        Args:
            pose (list): Posição do robô : [x, y, z, rx, ry, rz]
            positionType (int): 0 para posição por juntas, 1 para posição por coordenadas cartesianas
            
        Returns:
            bool: True se enviou, False se não enviou
        """
        #pose -> array da posição do robô com 6 elementos
        #type -> 0 para posição por juntas, 1 para posição por coordenadas cartesianas
        # Implement this method to send a pose to the robot
        if self._robot:
            self._robot.setPositionReg(pose, positionType)
            return True
        else:
            return False
            # raise Exception("O robô não existe na classe de integração externa. -> " + str(self))
        
    
    def runCodeOnRobot(self) -> bool:
        """
        Executa um código no robô (Implementação da interface)
        
        Returns:
            bool: True se executou, False se não executou
        """
        # Implement this method to run a code on the robot
        
        prog = """
        socket_open("127.0.0.1",30003)
        while (read_input_float_register(7) == 1):
        # while (1):
        
                socket_send_string("set speed")
                socket_send_string({})
                socket_send_byte(10)
                
                if (read_input_float_register(6) == 1):
                    tempPosition = p[read_input_float_register(0),
                            read_input_float_register(1),
                            read_input_float_register(2),
                            read_input_float_register(3),
                            read_input_float_register(4),
                            read_input_float_register(5)]
                    position = get_inverse_kin(tempPosition)
                else:
                    position = [read_input_float_register(0),
                            read_input_float_register(1),
                            read_input_float_register(2),
                            read_input_float_register(3),
                            read_input_float_register(4),
                            read_input_float_register(5)]
                end
                
                
                servoj(position, lookahead_time=0.2, gain=300)
                sync()
        end
        
        socket_close()

    """.format(self._robotSpeed)
        
        if self._robot:
            self._robot.robotConnector.RTDE.setData('input_double_register_7', 1) #Seta registrador que mantém o código em loop no controlador do robô
            self._robot.robotConnector.RTDE.sendData() #Envia o dado
            self._robot.robotConnector.RealTimeClient.SendProgram(prog)
            return True
        else:
            return False
    
    def stopCodeOnRobot(self) -> bool:
        """
        Para a execução de um código no robô (Implementação da interface)
        
        Returns:
            bool: True se parou, False se não parou
        """
        # Implement this method to stop a running code on the robot
        if self._robot:
            self._robot.robotConnector.RTDE.setData('input_double_register_7', 0) #Rseta registrador que mantém o código em loop
            self._robot.robotConnector.RTDE.sendData() #Envia o dado
            time.sleep(0.2)
            return True
        else:
            return False


class Ur5eCommMock(RobotExternalInterface):
    
    def __init__(self,):
        pass

    
    def connectToRobot(self) -> bool:
        return True
    
    def disconnectFromRobot(self) -> bool:
        return True
        
    
    def getTcpPositionFromRobot(self) -> list:
        return [1.308       ,0.202    ,0.15   , 1.775  ,-2.593 ,-0.013]
    
    def getTcpForceFromRobot(self) -> list:
        return [0.308       ,0.202    ,0.15   , 1.775  ,-2.593 ,-0.013]
    
    def sendPositionToRobot(self, pose: list, positionType: int) -> bool:
        return True
        
    
    def runCodeOnRobot(self) -> bool:
        return True
    
    def stopCodeOnRobot(self) -> bool:
        return True
    
    