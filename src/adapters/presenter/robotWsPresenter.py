from src.pkg.interfaces.adapterInterface import RobotAdapterInterface
from src.core.entities.Robot import Robot
import json

class robotWsPresenter(RobotAdapterInterface):
    """
    Apresentador de dados do robô, para conexões externas via websocket.
    Transforma a entidade do robô em um dicionário JSON.
    
    Methods:
        adaptData(robot: Robot) -> str: Adapta os dados do robô
    """
    def __init__(self):
        """
        Apresentador de dados do robô, para conexões externas via websocket.
        Transforma a entidade do robô em um dicionário JSON.
        """
        pass

    def adaptData(self, robot: Robot):
        """
        Adapta os dados do robô para uma json com as informações em um objeto lista.
        
        Args:
            robot (Robot): Entidade do robô
            
        Returns:
            str: JSON com as informações do robô
        """
        data = {
            "tcpPosition": robot.tcpPosition.tolist(),
            "tcpForce": robot.tcpForce.tolist(),
        }
        
        return json.dumps(data)


class robotWsPresenterLib(RobotAdapterInterface):
    """
    Apresentador de dados do robô, para conexões externas via websocket.
    Transforma a entidade do robô em um objeto com as informações em string.
    
    Methods:
        adaptData(robot: Robot) -> str: Adapta os dados do robô
    """
    def __init__(self):
        """
        Apresentador de dados do robô, para conexões externas via websocket.
        Transforma a entidade do robô em um objeto com as informações em string.
        """
        pass

    def adaptData(self, robot: Robot):
        """
        Adapta os dados do robô para um objeto com as informações em string.
        
        Args:
            robot (Robot): Entidade do robô
            
        Returns:
            object: Objeto com as informações
        """
        data = {
            "tcpPosition": str(robot.tcpPosition),
            "tcpForce": str(robot.tcpForce),
        }
        
        return data

class robotRawPresenter(RobotAdapterInterface):
    """
    Apresentador de dados do robô, para conexões externas.
    Retorna a entidade robô, da mesma maneira que ela existe dentro da arquitetura.
    
    Methods:
        adaptData(robot: Robot) -> str: Adapta os dados do robô
    """
    def __init__(self):
        """
        Apresentador de dados do robô, para conexões externas.
        Retorna a entidade robô, da mesma maneira que ela existe dentro da arquitetura.
        """
        pass
    def adaptData(self, robot: Robot):
        """
            Retorna os dados do robô sem formatação.

            Args:
            robot (Robot): Entidade do robô

            Returns:
            robot (Robot): Entidade do robô
        """
        return robot 