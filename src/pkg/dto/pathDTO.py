from dataclasses import dataclass

@dataclass
class PathDTO:  
    """
    DTO para informações de caminho do robô.
    
    Attributes:
        totalTime (int): Tempo total
        poseInit (list): Pose inicial
        poseDesired (list): Pose desejada
        nextPose (list): Próxima pose
    """  
    totalTime: int
    poseInit: list
    poseDesired: list
    nextPose: list
    