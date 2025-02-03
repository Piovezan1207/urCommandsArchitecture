from abc import ABC, abstractmethod
from src.pkg.dto.robotDTO import RobotDTO

class RobotExternalInterface():
    """
    Interface referente a integração com o robô fisico.
    
    Methods:
        getTcpPositionFromRobot() -> list: Retorna a posição do TCP do robô
        getTcpForceFromRobot() -> list: Retorna a força do TCP do robô
        sendPositionToRobot(pose: list, positionType: int) -> bool: Envia uma posição ao robô
        runCodeOnRobot() -> bool: Roda o código no robô
        stopCodeOnRobot() -> bool: Para a execução do código no robô
        connectToRobot() -> bool: Conecta com o robô
        disconnectFromRobot() -> bool: Desconecta do robô
    
    """
    @abstractmethod
    def getTcpPositionFromRobot() -> list: return list
    
    @abstractmethod
    def getTcpForceFromRobot() -> list: return list
    
    @abstractmethod
    def sendPositionToRobot(self, pose: list, positionType: int ) -> bool: return bool
    
    @abstractmethod
    def runCodeOnRobot(self) -> bool: return bool
    
    @abstractmethod
    def stopCodeOnRobot(self) -> bool: return bool
    
    @abstractmethod
    def connectToRobot(self) -> bool: return bool
    
    @abstractmethod
    def disconnectFromRobot(self) -> bool: return bool
    
class RoboDataExternalInterface():
    """
    Interface referente a utilização do repositorio de dados.
    
    Methods:
        saveRobotInformations(robotDTO: RobotDTO) -> RobotDTO: Salva as informações do robô
        loadRobotInformations() -> RobotDTO: Carrega as informações do robô
    """
    
    @abstractmethod
    def saveRobotInformations(self, robotDTO: RobotDTO) -> RobotDTO: return None
    
    @abstractmethod
    def loadRobotInformations(self) -> RobotDTO: return None