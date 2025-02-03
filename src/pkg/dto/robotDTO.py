from dataclasses import dataclass
from src.pkg.dto.pathDTO import PathDTO

@dataclass
class RobotDTO:    
    """
    DTO para informações do robô.
    
    Attributes:
        isConnected (bool): Conectado ou não
        codeIsRuunig (bool): Código rodando ou não
        lastPositionSendTime (int): Último tempo de envio de posição
        path (PathDTO): Informações de caminho
    """
    isConnected : bool 
    codeIsRuunig : bool
    lastPositionSendTime: int
    path: PathDTO
    
    