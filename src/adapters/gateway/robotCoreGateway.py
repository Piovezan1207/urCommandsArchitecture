from src.pkg.interfaces.gatewayInterfaces import RobotGatewayInterface
from src.pkg.interfaces.externalInterfaces import RobotExternalInterface

class RobotCoreGateway(RobotGatewayInterface):
    """
    Gateway de comunicação com o robô. Essa classe implementa a interface RobotGatewayInterface,
    e utiliza as classes de integração com o robô para fazer a comunicação com o mesmo.
    
    Args:
        robotExternal (RobotExternalInterface): Interface de comunicação com o robô
    
    Methods:
        connect(): Conecta com o robô
        disconnect(): Desconecta do robô
        runCode(): Roda o código no robô
        stopCode(): Para a execução do código no robô
        sendPose(pose: list, positionType: int): Envia uma posição ao robô
        getTcpPose(): Retorna a posição do TCP do robô
        getTcpForce(): Retorna a força do TCP do robô
    """
    def __init__(self, robotExternal: RobotExternalInterface):
        """
        Gateway de comunicação com o robô. Essa classe implementa a interface RobotGatewayInterface,
        e utiliza as classes de integração com o robô para fazer a comunicação com o mesmo.
    
        Args:
            robotExternal (RobotExternalInterface): Interface de comunicação com o robô
        """
        self._robotExternal = robotExternal
        
    def connect(self) -> bool:
        """
        Conecta com o robô.
        
        Returns:
            bool: True se conectou, False se não conectou
        """
        return self._robotExternal.connectToRobot()
    
    def disconnect(self) -> bool:
        """
        Desconecta do robô.
        
        Returns:
            bool: True se desconectou, False se não desconectou
        """
        return self._robotExternal.disconnectFromRobot()
    
    def runCode(self) -> bool:
        """
        Implementa metodos externos para rodar o código no robô.
        
        Returns: 
            bool: True se rodou, False se não rodou
        """
        return self._robotExternal.runCodeOnRobot()
    
    def stopCode(self) -> bool:
        """
        Implementa metodos externos para rodar parar de rodar o código no robô.
        
        Returns: 
            bool: True se parou, False se não parou
        """
        return self._robotExternal.stopCodeOnRobot()
    
    def sendPose(self, pose: list, positionType: int) -> bool:
        """
        Implementa metodos externos para enviar uma posição ao robô.
        
        Returns: 
            bool: True se enviou, False se não enviou
        """
        return self._robotExternal.sendPositionToRobot(pose, positionType)
    
    def getJointPose(self) -> list:
        """
        Implementa metodos externos para ler a posição de juntas do robô.
        
        Returns: 
            bool: True se obteve suscesso na leitura, False se não obteve
        """
        return self._robotExternal.getJointPositionFromRobot()
    
    def getTcpPose(self) -> list:
        """
        Implementa metodos externos para ler a posição TCP do robô.
        
        Returns: 
            bool: True se obteve suscesso na leitura, False se não obteve
        """
        return self._robotExternal.getTcpPositionFromRobot()
    
    def getTcpForce(self) -> list:
        """
        Implementa metodos externos para ler a força TCP do robô.
        
        Returns: 
            bool: True se obteve suscesso na leitura, False se não obteve
        """
        return self._robotExternal.getTcpForceFromRobot()
    
        
        