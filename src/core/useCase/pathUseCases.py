from src.core.entities.Path import Path
from src.core.entities.Robot import Robot

import math
import numpy as np

class PathUseCases(object):
    """
    Use cases referentes a criação d euma rota para o robô seguir.
    
    Methods:
        calculatePointDistance(p1: list, p2: list): Calcula a distância entre dois pontos
        calculateTimeBySpeed(distance: float, speed: float): Calcula o tempo de movimentação do robô
        createRobotPath(poseInit: list, poseDesired: list , speed : float = 0.1): Cria um path para o robô seguir
        calculateTrajectoryRobotPoint(path: Path, t : float) -> list: Calcula a trajetória
    """
    @staticmethod
    def calculatePointDistance(p1: list, p2: list):
        """
        Calcula a distancia entre 2 pontos em um plano cartesiano tridimensional.
        
        Args:
            p1 (list): Ponto 1
            p2 (list): Ponto 2
            
        Returns:
            float: Distância entre os pontos
        """
        x1, y1, z1 = p1[:3]
        x2, y2, z2 = p2[:3]
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        return dist
    
    @staticmethod
    def calculateTimeBySpeed(distance: float, speed: float):
        """
        Calcila o tempo de movimentação do robo, com base na velocidade e na distância a ser percorrida.
        
        Args:
            distance (float): Distância a ser percorrida
            speed (float): Velocidade do robô
        
        Returns:
            float: Tempo de movimentação
        """
        time = distance / speed
        return time
    
    @staticmethod
    def createRobotPath(poseInit: list, poseDesired: list , speed : float = 0.1):
        """
        Quando um path é criado, ele terá a posição atual como 
        inicio, destino e proxima posição. Isso garante que o robô irá ficar
        parado, mesmo que seu loop de envio de posição já teha sido iniciado.
        
        Args:
            poseInit (list): Pose inicial
            poseDesired (list): Pose desejada
            speed (float, optional): Velocidade do robô. Defaults to 0.1.
        
        Returns:
            path: Path do robô
        """
        nextPose = poseInit
        if poseDesired is None:
            poseDesired = poseInit
        totalTime = PathUseCases.calculateTimeBySpeed(PathUseCases.calculatePointDistance(poseInit, poseDesired), speed)  
        path = Path(totalTime, poseInit, poseDesired, nextPose) 
        return path
        
    
    @staticmethod
    def calculateTrajectoryRobotPoint(path: Path, t : float) -> list:
        """
        calcula o ponto em uma trajetória, no tempo t
        
        Args:
            path (Path): Path do robô
            t (float): Tempo
            
        Returns:
            list: Ponto da trajetória
        """
        X_init = path.poseInit[0]
        Y_init = path.poseInit[1]
        Z_init = path.poseInit[2]

        X_final = path.poseDesired[0]
        Y_final = path.poseDesired[1]
        Z_final = path.poseDesired[2]

        # position
        # x_traj = (X_final - X_init) / (path.totalTime ** 3) * (
        #         6 * (t ** 5) / (path.totalTime ** 2) - 15 * (t ** 4) / path.totalTime + 10 * (t ** 3)) + X_init
        # y_traj = (Y_final - Y_init) / (path.totalTime ** 3) * (
        #         6 * (t ** 5) / (path.totalTime ** 2) - 15 * (t ** 4) / path.totalTime + 10 * (t ** 3)) + Y_init
        # z_traj = (Z_final - Z_init) / (path.totalTime ** 3) * (
        #         6 * (t ** 5) / (path.totalTime ** 2) - 15 * (t ** 4) / path.totalTime + 10 * (t ** 3)) + Z_init
        
        x_traj = (X_final - X_init) / path.totalTime * t + X_init
        y_traj = (Y_final - Y_init) / path.totalTime * t + Y_init
        z_traj = (Z_final - Z_init) / path.totalTime * t + Z_init
        
        position = np.array([x_traj, y_traj, z_traj, 1.775  ,-2.593 ,-0.013 ])
        
        return position
    