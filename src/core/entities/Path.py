class Path:
    """
    Entidade path, referente as as rotas que o robô deve fazer em movimentações lineares para posições TCP.
    
    Args:
        totalTime (int): Tempo total de movimentação.
        poseInit (list): Pose inicial.
        poseDesired (list): Pose desejada.
        nextPose (list): Próxima
        
    Attributes:
        totalTime (int): Tempo total de movimentação.
        poseInit (list): Pose inicial.
        poseDesired (list): Pose desejada.
        nextPose (list): Próxima
    """
    def __init__(self,
                 totalTime: int,
                 poseInit: list,
                 poseDesired: list,
                 nextPose: list):
        
        """
        Entidade path, referente as as rotas que o robô deve fazer em movimentações lineares para posições TCP.
    
        Args:
            totalTime (int): Tempo total de movimentação.
            poseInit (list): Pose inicial.
            poseDesired (list): Pose desejada.
            nextPose (list): Próxima
        """
        
        self._totalTime = totalTime
        self._poseInit = poseInit
        self._poseDesired = poseDesired
        self._nextPose = nextPose
        
    @property
    def totalTime(self):
        return self._totalTime
    
    @totalTime.setter
    def totalTime(self, value):
        if value < 0:
            raise ValueError("Total time must be a positive integer.")
        self._totalTime = value
    
    @property
    def poseInit(self):
        return self._poseInit
    
    @poseInit.setter
    def poseInit(self, value):
        if len(value) != 6:
            raise ValueError("Initial pose must be a 6-dimensional list.")
        self._poseInit = value
    
    @property
    def poseDesired(self):
        return self._poseDesired
    
    @poseDesired.setter
    def poseDesired(self, value):
        if len(value) != 6:
            raise ValueError("Desired pose must be a 6-dimensional list.")
        self._poseDesired = value
        
    @property
    def nextPose(self):
        return self._nextPose
    
    @nextPose.setter
    def nextPose(self, value):
        if len(value) != 6:
            raise ValueError("Next pose must be a 6-dimensional list.")
        self._nextPose = value
        
        