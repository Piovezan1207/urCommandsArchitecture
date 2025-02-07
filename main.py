"""
Movimentação do UR5e para posições diversas, com sistema de planejamento de rotas para movimentação.
- Existe a necessidade de manter um loop que enviara as posições da da rota de acordo com o tempo.
- Esse código é uma sugestão de aplicaçãodesse sistema de planejamento de rotas, se utilizando de uma thread que será
a responsável por ennviar as posições ao robô.
"""

import threading
from src.external.datasource.ur5eObj import Ur5eObj #Datasurce do robo (nesse caso, o UR5e)
from src.external.integrations.ur5eComm import Ur5eComm, Ur5eCommMock #Classe de comunicação com o robo e a mesma classe mockada, para testes sem o robô fisico.
from src.adapters.presenter.robotWsPresenter import robotWsPresenter #Presenter de dados do robô para envio ao websocket (ws Não implementado nese exemplo)
from src.adapters.controller.robotController import RobotController #Controller do robô, que faz a comunicação com o datasource e a integração com o robo fisico, aplicando as regras de negócio.
import time

# from src.external.integrations.mitsubishConn import mitsubishConn

#Função que irá enviar as posições ao robô em tempo real, em segundo plano.
def getRobotPositionsRealTime(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados):
    while not stop_event.is_set():
        info = RobotController.getRobotInfo(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados)
        print(info)
        
stop_event = threading.Event()

# [-0.1256497542010706, -1.5887053648578089, -2.1571314970599573, -1.008080784474508, 1.5536009073257446, -0.3029282728778284]

##############################################################################################################

#Inicialização de variáveis e objetos

comunicacaoComRobo = Ur5eComm("192.168.12.248", robotSpeed=0.6) #Integração com o robô físico
# comunicacaoComRoboMock = Ur5eCommMock() #Integração com o robô físico
registroDadosRobo = Ur5eObj() #Datasource do robô
apresentadorDeDados = robotWsPresenter() #Presenter de dados do robô

##############################################################################################################

#Conectar com o robô
conectar = RobotController.connectToRobot(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados) #Conecta com o robô
print(conectar)
# rodarCodigo = RobotController.runCode(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados) #Roda o código no robô
# print(rodarCodigo)

#Iniciar thread de envio de posições ao robô
dataThread = threading.Thread(target=getRobotPositionsRealTime, args=(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados))
dataThread.start()

while True:
    pass

#Lista de posições que o robô irá se movimentar
randomPoseList = [ 
                    [0.308       ,0.202    ,0.15   , 1.775  ,-2.593 ,-0.013],
                    [0.192     ,0.256     ,0.15   , 1.775  ,-2.593 ,-0.013],
                    [0.094     ,0.243   , 0.167    , 1.775  ,-2.593 ,-0.013],
                    [0.308     ,0.145   , 0.430    , 1.775  ,-2.593 ,-0.013],
                    [0.129  ,0.288 , 0.182,           1.775  ,-2.593 ,-0.013],
                    [0.129 ,0.243   ,0.148 ,            1.775  ,-2.593 ,-0.013],
                    [0.048   ,0.293    ,0.195  ,            1.775  ,-2.593 ,-0.013],
                    [0.308       ,0.202    ,0.16   ,        1.775  ,-2.593 ,-0.013],
                    [0.308       ,0.202    ,0.15   , 1.775  ,-2.593 ,-0.013],
                    [0.192     ,0.256     ,0.15   , 1.775  ,-2.593 ,-0.013],
                    [0.094     ,0.243   , 0.167    , 1.775  ,-2.593 ,-0.013],
                    [0.308     ,0.145   , 0.430    , 1.775  ,-2.593 ,-0.013],
                    [0.129  ,0.288 , 0.182,           1.775  ,-2.593 ,-0.013],
                    [0.129 ,0.243   ,0.148 ,            1.775  ,-2.593 ,-0.013],
                    [0.048   ,0.293    ,0.195  ,            1.775  ,-2.593 ,-0.013],
                    [0.308       ,0.202    ,0.16   ,        1.775  ,-2.593 ,-0.013],
                    ]


#Movimentar o robô para as posições da lista
for posicao in randomPoseList: 
    novaPosicao = RobotController.moveTcp(comunicacaoComRobo, registroDadosRobo, poseDesired=posicao , speed = 0.13 ) 
    time.sleep(0.2)
time.sleep(1)

# Sinalizar para a thread parar
stop_event.set()
# Esperar a thread finalizar
dataThread.join()

#Desconectar do robô
desconectar = RobotController.disconnectFromRobot(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados)
print(desconectar)