import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 61

def log(msg):
    """Função simples de log."""
    print(f"[LOG] {msg}")

def atender_cliente(conn, addr):
    log(f"Cliente conectado: {addr}")

    try:
        while True:
            requisicao = conn.recv(1024)
            if not requisicao:
                break

            hora_atual = datetime.now().strftime("%H:%M:%S")
            log(f"Solicitação de {addr} atendida com hora: {hora_atual}")

            conn.sendall(hora_atual.encode("utf-8"))
    except Exception as e:
        log(f"Erro com cliente {addr}: {e}")
    finally:
        log(f"Cliente desconectado: {addr}")
        conn.close()

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    log(f"Servidor de Hora ativo em {HOST}:{PORT}")

    while True:
        try:
            conn, addr = servidor.accept()
            thread = threading.Thread(target=atender_cliente, args=(conn, addr))
            thread.start()
        except Exception as e:
            log(f"Erro no servidor: {e}")

if __name__ == "__main__":
    main()
