from abc import ABCMeta, abstractmethod
from src.core.entities.Robot import Robot

class RobotGatewayInterface():
    """
    Interface referente ao gateway de utilização de metodos externos do robô.
    
    Methods:
        connect() -> bool: Conecta com o robô
        disconnect() -> bool: Desconecta do robô
        runCode() -> bool: Roda o código no robô
        stopCode() -> bool: Para a execução do código no robô
        sendPose(pose: list, positionType: int) -> bool: Envia uma posição ao robô
        getTcpPose() -> list: Retorna a posição do TCP do robô
        getTcpForce() -> list: Retorna a força do TCP do robô
    """
    @abstractmethod
    def connect(self) -> bool: return None #Deve retirnar o status da conexão
    
    @abstractmethod
    def disconnect(self) -> bool: return None #Deve retirnar o status da desconexão
    
    @abstractmethod
    def getJointPose(self) -> list: return  None
    
    @abstractmethod
    def getTcpPose(self) -> list: return  None
    
    @abstractmethod
    def getTcpForce(self) -> list: return  None
    
    @abstractmethod
    def runCode(self) -> bool: return None
    
    @abstractmethod
    def stopCode(self) -> bool: return None
    
    @abstractmethod
    def sendPose(self, pose: list, positionType: int) -> bool: return None
    
class RoboDataGatewayInterface():
    """
    Interface referente ao gateway de utilização do repositorio de dados.
    
    Methods:
        save(robot: Robot) -> Robot: Salva as informações do robô
        load() -> Robot: Carrega as informações do robô
    """
    @abstractmethod
    def save(self, robot: Robot) -> Robot: return None
    
    @abstractmethod
    def load(self) -> Robot: return None