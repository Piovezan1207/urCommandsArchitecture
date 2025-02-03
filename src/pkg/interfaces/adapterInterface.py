from abc import ABC, abstractmethod
from src.core.entities.Robot import Robot

class RobotAdapterInterface():
    """
    Interface referente aos adapters, responsáveis por formata o dado da entidade robô,
    para utilização fora da arquitetura.
    
    Methods:
        adaptData(robot: Robot) -> str: Adapta os dados do robô
    """
    @abstractmethod
    def adaptData(robot: Robot) -> str: return 