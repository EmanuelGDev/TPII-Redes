import socket
import threading

HOST = "127.0.0.1"
PORT = 61

clientes = []

def encaminhar(mensagem, remetente):
    """Envia a mensagem para o outro cliente conectado."""
    for c in clientes:
        if c != remetente:
            try:
                c.sendall(mensagem)
            except:
                pass

def lidar_com_cliente(conn, addr):
    print(f"[CONECTADO] Cliente: {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            encaminhar(msg, conn)
        except:
            break

    print(f"[DESCONECTADO] {addr}")
    clientes.remove(conn)
    conn.close()

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(2)

    print("[SERVIDOR ATIVO] Aguardando 2 clientes...")

    # Aceitar exatamente dois clientes
    while len(clientes) < 2:
        conn, addr = servidor.accept()
        clientes.append(conn)
        thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
        thread.start()

    print("[CHAT INICIADO] Dois clientes conectados. Mensagens serão repassadas.")

if __name__ == "__main__":
    main()
