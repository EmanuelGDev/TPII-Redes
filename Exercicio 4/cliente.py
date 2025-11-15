import socket

HOST = "127.0.0.1"
PORT = 61

def main():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORT))

        cliente.sendall(b"hora")

        hora = cliente.recv(1024).decode("utf-8")
        print(f"Hora recebida do servidor: {hora}")

        cliente.close()
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
