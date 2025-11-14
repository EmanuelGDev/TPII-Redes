import socket

HOST = "0.0.0.0"
PORT = 6000
MAX_SIZE = 65507

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORT))
    servidor.settimeout(1)  # <-- IMPORTANTE!

    print(f"[SERVIDOR UDP] Escutando em {HOST}:{PORT}")

    try:
        while True:
            try:
                msg, addr = servidor.recvfrom(MAX_SIZE)
                print(f"[RECEBIDO de {addr}] {msg.decode('utf-8')}")
                servidor.sendto(msg, addr)

            except socket.timeout:
                # Timeout normal: apenas permite que Ctrl+C seja detectado
                continue

    except KeyboardInterrupt:
        print("\n[SERVIDOR] Fechando com segurança...")
    finally:
        servidor.close()

if __name__ == "__main__":
    main()
