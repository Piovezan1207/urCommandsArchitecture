from src.core.entities.Robot import Robot
from src.core.entities.Path import Path
from src.pkg.interfaces.gatewayInterfaces import RobotGatewayInterface, RoboDataGatewayInterface

from src.core.useCase.pathUseCases import PathUseCases
import time

class RobotUseCases():
    
    @staticmethod
    def runCodeOnRobot(robot: Robot, robotGateway: RobotGatewayInterface):
        """
        Roda o código de leitura de posições e movimento no robô.
        
        Args:
            robot (Robot): Robô
            robotGateway (RobotGatewayInterface): Gateway de comunicação com o robô
            
        Returns:
            Robot: Entidade do robô
        """
        if robot.isConnected:
            status = robotGateway.runCode()
            if status:
                robot.codeIsRuunig = True
            else:
                raise Exception("Falha ao rodar código no robô.")
        else:
            raise Exception("O robô deve estar conectado para que o código seja enviado.")    
        return robot
    
    @staticmethod
    def sendPosToRobot(robot: Robot, pose: list, positionType: int, robotGateway: RobotGatewayInterface):
        """
        Envia uma posição ao robô.
        
        Args:
            robot (Robot): Robô
            pose (list): Posição
            positionType (int): Tipo de posição
            robotGateway (RobotGatewayInterface): Gateway de comunicação com o robô
        
        Returns:
            Robot: Entidade do robô
        """
        if robot.isConnected:
            # print(PathUseCases.calculatePointDistance(robot.tcpPosition, pose))
            status = robotGateway.sendPose(pose, positionType)
            # if status:
            #     robot.lastPositionSendTime = time.time()
            # else:
            #     raise Exception("Falha ao enviar posição ao robô.")
        else:
            raise Exception("O robô deve estar conectado para a posição ser enviada.")

        return robot
    
    @staticmethod
    def getRobotInfo(robot: Robot, robotGateway: RobotGatewayInterface):
        """
        Pega as informações do robô.
        
        Args:
            robot (Robot): Robô
            robotGateway (RobotGatewayInterface): Gateway de comunicação com o robô
        
        Returns:
            Robot: Entidade do robô
        """
        robot.tcpPosition = robotGateway.getTcpPose()
        robot.tcpForce = robotGateway.getTcpForce()
        return robot
    
    @staticmethod
    def getRobotData(RoboDataGateway: RoboDataGatewayInterface):
        """
        Carrega os daddos do robô que foram salvos.
        
        Args:
            RoboDataGateway (RoboDataGatewayInterface): Gateway de dados do robô
        
        Returns:
            Robot: Entidade do robô
        """
        robot = RoboDataGateway.load()
        return robot
    
    @staticmethod
    def stopCodeOnRobot(robot: Robot, robotGateway: RobotGatewayInterface):
        """
        Para a execução do código no robô.
        
        Args:
            robot (Robot): Robô
            robotGateway (RobotGatewayInterface): Gateway de comunicação com o robô
            
        Returns:
            Robot: Entidade do robô
        """
        if robot.isConnected:
            status = robotGateway.stopCode()
            if status:
                robot.codeIsRuunig = False
            else:
                raise Exception("Falha ao parar código no robô.")
        else:
            raise Exception("O robô deve estar conectado para que o código seja parado.")    
        return robot
    
    @staticmethod
    def connectToRobot(robot: Robot, robotGateway: RobotGatewayInterface):
        """
        Conecta ao robô.
        
        Args:
            robot (Robot): Robô
            robotGateway (RobotGatewayInterface): Gateway de comunicação com o robô
            
        Returns:
            Robot: Entidade do robô
        """
        if robot.isConnected:
            raise Exception("O robô já está conectado.")
        
        status = robotGateway.connect()
        
        if status:
            robot.isConnected = True
        else:
            raise Exception("Falha ao conectar ao robô.")
        
        return robot
    
    @staticmethod
    def disconnectFromRobot(robot: Robot, robotGateway: RobotGatewayInterface):
        """
        Desconecta do robô.
        
        Args:
            robot (Robot): Robô
            robotGateway (RobotGatewayInterface): Gateway de comunicação com o robô
        
        Returns:
            Robot: Entidade do robô
        """
        if not robot.isConnected:
            raise Exception("O robô já está desconectado.")
        
        status = robotGateway.disconnect()
        
        if status:
            robot.isConnected = False
        else:
            raise Exception("Falha ao desconectar do robô.")
        
        return robot

    @staticmethod
    def setRobotPath(path: Path, robot: Robot):
        """
        Seta um path na entidade robô.
        
        Args:
            path (Path): Path
            robot (Robot): Robô
        
        Returns:
            Robot: Entidade do robô
        """
        robot.path = path
        return robot
        
    
    
    @staticmethod
    def saveRobotInfo(robot: Robot, roboDataGateway: RoboDataGatewayInterface):
        """
        Salva as informações do robô.
        
        Args:
            robot (Robot): Robô
            roboDataGateway (RoboDataGatewayInterface): Gateway de dados do robô
        
        Returns:
            Robot: Entidade do robô
        """
        robot = roboDataGateway.save(robot)
        return robot
    
 
