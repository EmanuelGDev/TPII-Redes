import socket
import threading

HOST = "127.0.0.1"
PORT = 61

def receber_msg(conexao):
    """Thread que fica ouvindo as mensagens recebidas."""
    while True:
        try:
            msg = conexao.recv(1024).decode("utf-8")
            if not msg:
                break
            print(f"\nMensagem: {msg}")
        except:
            break

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    print("Conectado ao servidor. Digite mensagens para enviar.")
    print("Digite 'sair' para encerrar.\n")

    # Thread de recebimento
    thread_recv = threading.Thread(target=receber_msg, args=(cliente,), daemon=True)
    thread_recv.start()

    while True:
        msg = input()
        if msg.lower() == "sair":
            cliente.close()
            print("Chat encerrado.")
            break

        cliente.sendall(msg.encode("utf-8"))

if __name__ == "__main__":
    main()
