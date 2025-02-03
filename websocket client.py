import websocket
import json
import time

class temp:
    
    initialTemp = 0
    
initialTempTime = temp()
initialTempTime.initialTemp = time.time() 

def on_message(ws, message):
    # print(time.time() - initialTempTime.initialTemp)
    print(f"Mensagem recebida: {message}")
    message = json.loads(message)
    # posicao = [message["X"],message["Y"],message["Z"],message["Pulse_1"],message["Pulse_2"],message["Pulse_3"]]
    posicao = [message["Base"],message["Shoulder"],message["Elbow"],message["Pulse_1"],message["Pulse_2"],message["Pulse_3"]]
    print(posicao)
    
    initialTempTime.initialTemp = time.time()

def on_error(ws, error):
    print(f"Erro: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Conexão fechada")

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
