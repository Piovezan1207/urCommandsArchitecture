from src.pkg.interfaces.externalInterfaces import RoboDataExternalInterface

from src.pkg.dto.robotDTO import RobotDTO 
from src.pkg.dto.pathDTO import PathDTO

class Ur5eObj(RoboDataExternalInterface):
    """
    Classe de datasource do UR5e. Essa classe implementa a interface RoboDataExternalInterface,
    nesse exemplo, os dados do robô ficam em memória, mas poderiam ser salvos em um banco de dados, por exemplo.
    
    Args:
        totalTime (int, optional): Tempo total de movimentação. Defaults to None.
        poseInit (list, optional): Pose inicial. Defaults to None.
        poseDesired (list, optional): Pose desejada. Defaults to None.
        nextPose (list, optional): Próxima pose. Defaults to None.
        isConnected (bool, optional): Conectado ou não. Defaults to None.
        codeIsRuunig (bool, optional): Código rodando ou não. Defaults to None.
        lastPositionSendTime (int, optional): Último tempo de envio de posição. Defaults to None.
        
    Methods:
        saveRobotInformations(robotDTO: RobotDTO): Salva as informações do robô
        loadRobotInformations(): Carrega as informações do robô
        
    """
    def __init__(self, totalTime: int = None,
                        poseInit: list= None,
                        poseDesired: list= None,
                        nextPose: list= None,
                        isConnected : bool = None,
                        codeIsRuunig : bool= None,
                        lastPositionSendTime: int = None):
        
        """
        Construtor da classe Ur5eObj
        
        Args:
            totalTime (int, optional): Tempo total de movimentação. Defaults to None.
            poseInit (list, optional): Pose inicial. Defaults to None.
            poseDesired (list, optional): Pose desejada. Defaults to None.
            nextPose (list, optional): Próxima pose. Defaults to None.
            isConnected (bool, optional): Conectado ou não. Defaults to None.
            codeIsRuunig (bool, optional): Código rodando ou não. Defaults to None.
            lastPositionSendTime (int, optional): Último tempo de envio de posição. Defaults to None.
        """
        
        self.totalTime = totalTime
        self.poseInit = poseInit
        self.poseDesired = poseDesired
        self.nextPose = nextPose
        self.isConnected = isConnected
        self.codeIsRuunig = codeIsRuunig
        self.lastPositionSendTime = lastPositionSendTime
    
    def saveRobotInformations(self, robotDTO: RobotDTO) -> RobotDTO:
        """
        Salva as informações do robô
        
        Args:   
            robotDTO (RobotDTO): Dados do robô
        
        Returns:
            RobotDTO: Dados do robô salvos
        """
        self.totalTime = robotDTO.path.totalTime
        self.poseInit = robotDTO.path.poseInit
        self.poseDesired = robotDTO.path.poseDesired
        self.nextPose = robotDTO.path.nextPose
        self.isConnected = robotDTO.isConnected
        self.codeIsRuunig = robotDTO.codeIsRuunig
        self.lastPositionSendTime = robotDTO.lastPositionSendTime
    

    def loadRobotInformations(self) -> RobotDTO:
        """
        Carrega as informações do robô
        
        Returns:
            RobotDTO: Dados do robô
        """
        #Implements this method to load robot informations
        pathDTO = PathDTO(self.totalTime,
                          self.poseInit,
                          self.poseDesired,
                          self.nextPose)
        
        robotDTO = RobotDTO(self.isConnected,
                            self.codeIsRuunig,
                            self.lastPositionSendTime,
                            pathDTO)
        
        return robotDTO
    
    

