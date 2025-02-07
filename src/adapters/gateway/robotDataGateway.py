from src.pkg.interfaces.gatewayInterfaces import RoboDataGatewayInterface
from src.pkg.interfaces.externalInterfaces import RoboDataExternalInterface

from src.core.entities.Robot import Robot
from src.core.entities.Path import Path

from src.pkg.dto.robotDTO import RobotDTO
from src.pkg.dto.pathDTO import PathDTO

class RobotDataGateway(RoboDataGatewayInterface):
    """
    Gateway para salvar e carregar informações do robô, a partir de implementações externas.
    
    Args:
        roboDataExternal (RoboDataExternalInterface): Implementação externa para salvar e carregar informações do robô
    
    Methods:
        save(robot: Robot): Salva as informações do robô
        load(): Carrega as informações do robô
    """
    def __init__(self, roboDataExternal: RoboDataExternalInterface):
        """
        Gateway para salvar e carregar informações do robô, a partir de implementações externas.
    
        Args:
            roboDataExternal (RoboDataExternalInterface): Implementação externa para salvar e carregar informações do robô
        """
        self._robotDataExternal = roboDataExternal
    
    def save(self, robot: Robot) -> Robot:
        """
        Salva as informações a partir da implementaçao de integração externa com repositorio de dados.
        
        Args:
            robot (Robot): Robô
        
        Returns:
            Robot: Entidade robot
        """
        
        pathDTO = PathDTO(robot.path.totalTime,
                          robot.path.poseInit,
                          robot.path.poseDesired,
                          robot.path.nextPose)
        
        robotDTO = RobotDTO(robot.isConnected,
                            robot.codeIsRuunig,
                            robot.lastPositionSendTime,
                            pathDTO)
        
        self._robotDataExternal.saveRobotInformations(robotDTO) 
        
        return robot
        
    def load(self) -> Robot: 
        """
        Carrega as informações a partir da implementaçao de integração externa com repositorio de dados.
        
        Returns:
            Robot: Entidade robot
        """
        robotDto = self._robotDataExternal.loadRobotInformations()
        
        path = Path(robotDto.path.totalTime,
                    robotDto.path.poseInit,
                    robotDto.path.poseDesired,
                    robotDto.path.nextPose)
        
        robot = Robot(None,
                      None,
                      None,
                      path,
                     robotDto.isConnected,
                     robotDto.codeIsRuunig,
                     robotDto.lastPositionSendTime)
        
        return robot