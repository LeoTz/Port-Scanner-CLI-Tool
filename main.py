import argparse
import socket
import threading

VERSION = "0.0.1"

def checkConnection(host_name, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = ""

    try:
        # sock.settimeout(1)
        sock.connect((host_name, port))
        result = "OPEN"
    # except (socket.error, socket.timeout):
    except socket.error as e:
        result = "CLOSE"
    finally:
        sock.close()

    print(f"{host_name} connection on port {port}: {result}")


parser = argparse.ArgumentParser(
    prog = "ps",
    description="Port Scanner CLI application. By: Timothy Joseph",
)

parser.add_argument(
    "--version",
    action="version", 
    version=f"Port SCanner CLI v{VERSION}",
)

parser.add_argument(
    "host_name",
    help="The name of the host for which possible connections are scanned for",
)

parser.add_argument(
    "-p",
    required=True,
    help="Ports of range of ports to scan for connections to provided host name"
)

args = parser.parse_args()

threads = []

# Splits the ports seperated by ','
if ',' in args.p:
    ports = args.p.split(',')
    ports = [int(port) for port in ports]
    # Checks the connection with the host name at the provided ports
    for port in ports:
        # checkConnection(args.host_name, port)
        t = threading.Thread(target=checkConnection, args=(args.host_name, port,))
        t.start()
        threads.append(t)
        
# splits the ports seperated by '-'
elif '-' in args.p:
    ports = args.p.split('-')
    ports = [int(port) for port in ports]
    # Checks the connection with the host name at the provided range of ports
    for port in range(ports[0], ports[1]+1):
        # checkConnection(args.host_name, port)
        t = threading.Thread(target=checkConnection, args=(args.host_name, port,))
        t.start()
        threads.append(t)
else:
    checkConnection(args.host_name, int(args.p))

for thread in threads:
    thread.join()
