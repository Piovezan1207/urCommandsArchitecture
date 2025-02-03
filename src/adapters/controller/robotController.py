#Interfaces para conexões externas
from src.pkg.interfaces.externalInterfaces import RobotExternalInterface, RoboDataExternalInterface
from src.pkg.interfaces.adapterInterface import RobotAdapterInterface

#Gateways para interação do core com os dados externos
from src.adapters.gateway.robotCoreGateway import RobotCoreGateway
from src.adapters.gateway.robotDataGateway import RobotDataGateway

#Use Cases para aplicação da lógica
from src.core.useCase.robotUseCases import RobotUseCases
from src.core.useCase.pathUseCases import PathUseCases 

#Presenters para adaptação dos dados e apresentação dos mesmos
from src.adapters.presenter.robotWsPresenter import robotWsPresenter, robotRawPresenter

#Bibliotecas
import time

class RobotController():
    """
    Classe de controle do robô. Essa classe é responsável por controlar as ações do robô,
    como conectar, desconectar, enviar posições, rodar código, parar código, entre outros.
    
    Todas as ações são construidas com a utilização dos usecases.
    
    Args:
        robotExternal (RobotExternalInterface): Interface de comunicação com o robô
        roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
        robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
        
    Methods:
        connectToRobot(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): Conecta com o robô
        disconnectFromRobot(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): Desconecta do robô
        runCode(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): Roda um código no robô
        stopCode(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): Para a execução de um código no robô
        moveTcp(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter(), poseDesired = None, speed = 0.1): Move o robô por TCP
        sendTcpSequencPathPositions(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): Envia as posições da rota ao robô
        moveJoint(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter(), poseDesired: list = None): Move o robô por Joint
        getRobotInfo(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): Retorna as informações do robô
    """
    @staticmethod
    def connectToRobot(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()):
        """
        Construção da lógica para conectar com o robô
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
        
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        """
        robotGateway = RobotCoreGateway(robotExternal)
        robotDataGateway = RobotDataGateway(roboDataExternal)
        
        robot = RobotUseCases.getRobotData(robotDataGateway)
        
        robot = RobotUseCases.connectToRobot(robot, robotGateway)
        
        
        robot = RobotUseCases.saveRobotInfo(robot, robotDataGateway)
        
        robot = RobotController.runCode(robotExternal, roboDataExternal)
        
        print(robot)
        return robotPresenter.adaptData(robot)


    @staticmethod
    def disconnectFromRobot(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): 
        """
        Construção da lógica para desconectar do robô
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
        
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        """
        robotGateway = RobotCoreGateway(robotExternal)
        robotDataGateway = RobotDataGateway(roboDataExternal)
        
        robot = RobotController.stopCode(robotExternal, roboDataExternal)
        
        robot = RobotUseCases.disconnectFromRobot(robot, robotGateway)
        robot = RobotUseCases.saveRobotInfo(robot, robotDataGateway)
        
        return robotPresenter.adaptData(robot)
    
    @staticmethod
    def runCode(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()):
        """
        Construção da lógica para rodar um código no robô
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
        
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        
        """
        robotGateway = RobotCoreGateway(robotExternal)
        robotDataGateway = RobotDataGateway(roboDataExternal)
        
        robot = RobotController.getRobotInfo(robotExternal, roboDataExternal)
        
        actualPose = robot.tcpPosition
        print("Posição atual no momento da conexão", actualPose)
        
        robot = RobotUseCases.sendPosToRobot(robot, actualPose, 1,robotGateway)
        robot = RobotUseCases.runCodeOnRobot(robot, robotGateway) 
        robot = RobotUseCases.saveRobotInfo(robot, robotDataGateway)
        
        return robotPresenter.adaptData(robot)
    
    @staticmethod
    def stopCode(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): 
        """
        Construção da lógica para parar a execução de um código no robô
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
        
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        """
        robotGateway = RobotCoreGateway(robotExternal)
        robotDataGateway = RobotDataGateway(roboDataExternal)
        
        robot = RobotController.getRobotInfo(robotExternal, roboDataExternal)
        
        robot = RobotUseCases.stopCodeOnRobot(robot, robotGateway)
        robot = RobotUseCases.saveRobotInfo(robot, robotDataGateway)
        
        return robotPresenter.adaptData(robot)
    
    @staticmethod 
    def moveTcp(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter(), poseDesired = None, speed = 0.1): 
        """
        Construção da lógica para mover o robô por TCP
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
            poseDesired (list, optional): Pose desejada. Defaults to None.
            speed (float, optional): Velocidade do robô. Defaults to 0.1.
        
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        """
        robotGateway = RobotCoreGateway(robotExternal)
        robotDataGateway = RobotDataGateway(roboDataExternal)
        
        robot = RobotController.getRobotInfo(robotExternal, roboDataExternal)
        
        if poseDesired is None: poseDesired = robot.tcpPosition
        
        path = PathUseCases.createRobotPath(robot.tcpPosition, poseDesired, speed)
        
        robot = RobotUseCases.setRobotPath(path, robot)
        
        robot = RobotUseCases.saveRobotInfo(robot, robotDataGateway)
        
        RobotController.sendTcpSequencPathPositions(robotExternal, roboDataExternal, robotPresenter)
        
        return robotPresenter.adaptData(robot)
    
    @staticmethod
    def sendTcpSequencPathPositions(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()):
        """
        Sequencia de envio de posições ao robô
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
            
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        """
        robotGateway = RobotCoreGateway(robotExternal)
        robotDataGateway = RobotDataGateway(roboDataExternal)
        
        robot = RobotUseCases.getRobotData(robotDataGateway)
        
        t_start = time.time()
        t_final = robot.path.totalTime
        
        while time.time() - t_start < t_final:
            t_current = (time.time() ) - t_start
            position = PathUseCases.calculateTrajectoryRobotPoint(robot.path, t_current)
            robot = RobotUseCases.sendPosToRobot(robot, position, 1, robotGateway) #Movimento por TCP

        return robotPresenter.adaptData(robot)
    
    @staticmethod
    def moveJoint(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter(), poseDesired: list = None):
        """
        Sequencia logica para mover o robô por Joint
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
            poseDesired (list, optional): Pose desejada. Defaults to None.
            
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        """
        robotGateway = RobotCoreGateway(robotExternal)
        robotDataGateway = RobotDataGateway(roboDataExternal)
        
        robot = RobotUseCases.getRobotData(robotDataGateway)
        if poseDesired is None: poseDesired = robot.tcpPosition
    
        robot = RobotUseCases.sendPosToRobot(robot, poseDesired, 0, robotGateway) #Movimento por Joint
        
        return robotPresenter.adaptData(robot)
    
    @staticmethod
    def getRobotInfo(robotExternal: RobotExternalInterface, roboDataExternal: RoboDataExternalInterface, robotPresenter: RobotAdapterInterface = robotRawPresenter()): 
        """
        Trazer todas as informações do robô
        
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
            roboDataExternal (RoboDataExternalInterface): Interface de comunicação com os dados do robô
            robotPresenter (RobotAdapterInterface, optional): Presenter de dados do robô. Defaults to robotRawPresenter().
        
        Returns:
            RobotAdapterInterface: Dados do robô adaptados
        """
        robotGateway = RobotCoreGateway(robotExternal) 
        robotDataGateway = RobotDataGateway(roboDataExternal)
        robot = RobotUseCases.getRobotData(robotDataGateway)
        robot = RobotUseCases.getRobotInfo(robot, robotGateway)
        robot = RobotUseCases.saveRobotInfo(robot, robotDataGateway)
        return robotPresenter.adaptData(robot)
    

    