from src.core.entities.Path import Path
import time

class Robot:
    """
    Entidade Robot, representa o robô real, contendo todas as suas informações de posição, força e caminho.
    
    Args:
        tcpPosition (list): Posição do TCP.
        tcpForce (list): Força do TCP.
        path (Path): Caminho do robô.
        isConnected (bool): Flag de conexão.
        codeIsRuunig (bool): Flag de código rodando.
        lastPositionSendTime (float): Tempo da última posição enviada.
        
    """
    def __init__(self, 
                 tcpPosition: list,
                 tcpForce: list,
                 path: Path,
                 isConnected : bool = False,
                 codeIsRuunig : bool = False,
                 lastPositionSendTime = time.time()
                 ):

        """
        Entidade Robot, representa o robô real, contendo todas as suas informações de posição, força e caminho.
        
        Args:
            tcpPosition (list): Posição do TCP.
            tcpForce (list): Força do TCP.
            path (Path): Caminho do robô.
            isConnected (bool): Flag de conexão.
            codeIsRuunig (bool): Flag de código rodando.
            lastPositionSendTime (float): Tempo da última posição enviada.
            
        """

        self._isConnected = isConnected
        self._tcpPosition = tcpPosition
        self._tcpForce = tcpForce
        self._path = path
        self._codeIsRuunig = codeIsRuunig
        self._lastPositionSendTime = lastPositionSendTime
        
    @property
    def lastPositionSendTime(self) -> float:
        return self._lastPositionSendTime
    
    @lastPositionSendTime.setter
    def lastPositionSendTime(self, value: float):
        self._lastPositionSendTime = value

    @property
    def codeIsRuunig(self) -> bool:
        return self._codeIsRuunig
    
    @codeIsRuunig.setter
    def codeIsRuunig(self, value: bool):
        self._codeIsRuunig = value
    
    
    @property
    def isConnected(self) -> bool:
        return self._isConnected
    
    @isConnected.setter
    def isConnected(self, value: bool):
        self._isConnected = value
        
    @property
    def tcpPosition(self) -> list:
        return self._tcpPosition
    
    @tcpPosition.setter
    def tcpPosition(self, value: list):
        self._tcpPosition = value
    
    @property
    def tcpForce(self) -> list:
        return self._tcpForce
    
    @tcpForce.setter
    def tcpForce(self, value: list):
        self._tcpForce = value

    
    @property
    def path(self) -> Path:
        return self._path
    
    @path.setter
    def path(self, value: Path):
        self._path = value
        
    
    