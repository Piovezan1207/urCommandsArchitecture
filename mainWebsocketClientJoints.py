# from managedThread import ManagedThread

from src.external.datasource.ur5eObj import Ur5eObj
from src.external.integrations.ur5eComm import Ur5eComm, Ur5eCommMock
from src.adapters.presenter.robotWsPresenter import robotWsPresenter, robotWsPresenterLib

from src.adapters.controller.robotController import RobotController

import websocket
import json
import secrets
import time


class globalToken:
    value = secrets.token_hex(16)

token = globalToken()
print(token.value)
time.sleep(2)
    


comunicacaoComRobo = Ur5eComm("192.168.12.248", robotSpeed=0.6)
# comunicacaoComRobo = Ur5eCommMock()
registroDadosRobo = Ur5eObj()
apresentadorDeDados = robotWsPresenter()
apresentadorDeDadosLib = robotWsPresenterLib()

conectar = RobotController.connectToRobot(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados)
# novaPosicao = RobotController.moveTcp(comunicacaoComRobo, registroDadosRobo, poseDesired=json.loads(conectar)["tcpPosition"], speed = 0.13 ) 
# exit()
# novaPosicao = RobotController.moveTcp(comunicacaoComRobo, registroDadosRobo,  speed = 0.13 ) 
# print()

def on_message(ws, message):
    message = json.loads(message)
    # time.sleep(2)
    # print(time.time() - initialTempTime.initialTemp)
    # print(f"Mensagem recebida: {message}")
    
    info = RobotController.getRobotInfo(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados) #apresentadorDeDadosLib
    payload = {
        "Token": token.value,
        "data" : info
    }
    # print(payload)
    ws.send(json.dumps(payload))
    
    if message["Token"] != token.value:
        print("Token inválido")
        
        # RobotController.moveTcp(comunicacaoComRobo, registroDadosRobo, poseDesired = info["data"]["tcpPosition"], speed= 0.1)
        return 
    
    # posicao = [message["X"],message["Y"],message["Z"],message["Pulse_1"],message["Pulse_2"],message["Pulse_3"]]
    posicao = [message["Base"],message["Shoulder"],message["Elbow"],message["Pulse_1"],message["Pulse_2"],message["Pulse_3"]]
    # posicaoTcp = [message["X"],message["Y"],message["Z"]]
    print("Movendo para: ", posicao)
    RobotController.moveJoint(comunicacaoComRobo, registroDadosRobo, poseDesired = posicao)


def on_error(ws, error):
    print(f"Erro: {error}")

def on_close(ws, close_status_code, close_msg):
    time.sleep(1)
    # threadMovimento.stop()
    desconectar = RobotController.disconnectFromRobot(comunicacaoComRobo, registroDadosRobo, apresentadorDeDados)
    print(desconectar)

def on_open(ws):
    print("Conexão aberta")
    ws.send("Olá, servidor!")  # Envia uma mensagem ao abrir a conexão

# Criando a conexão WebSocket
# url = "ws://echo.websocket.org"  # Troque pela URL do servidor WebSocket
url = "ws://10.83.146.5:8080"  # Troque pela URL do servidor WebSocket
ws = websocket.WebSocketApp(
    url,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)

ws.on_open = on_open  # Configura o callback para quando abrir a conexão
ws.run_forever()      # Mantém o WebSocket ativo
