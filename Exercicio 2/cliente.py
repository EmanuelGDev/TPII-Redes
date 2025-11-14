import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 6000
MAX_SIZE = 65507  # limite UDP

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define timeout para evitar travamento caso o servidor não responda
    cliente.settimeout(3)

    print("Cliente UDP iniciado. Digite mensagens para enviar.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        msg = input("Mensagem: ")

        if msg.lower() == "sair":
            print("Encerrando cliente...")
            break

        # Validação do tamanho
        if len(msg.encode("utf-8")) > MAX_SIZE:
            print("❌ ERRO: Mensagem muito grande para UDP (máx 64KB).")
            continue

        try:
            # Envia mensagem ao servidor
            cliente.sendto(msg.encode("utf-8"), (SERVER_HOST, SERVER_PORT))

            # Aguarda resposta
            resposta, _ = cliente.recvfrom(MAX_SIZE)

            print("Eco do servidor:", resposta.decode("utf-8"))
        
        except socket.timeout:
            print("⚠️  Tempo limite: nenhuma resposta do servidor.")
        
        except Exception as e:
            print(f"Erro de comunicação: {e}")

    cliente.close()

if __name__ == "__main__":
    main()
