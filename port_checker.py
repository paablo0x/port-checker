import socket
import sys


def check_port(host, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        return sock.connect_ex((host, port)) == 0
    finally:
        sock.close()


if len(sys.argv) != 3:
    print(f"Usage: python port_checker.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

if check_port(host, port):
    print(f"[+] {host}:{port} is OPEN")
else:
    print(f"[-] {host}:{port} is CLOSED")