#!/usr/bin/python3
import socket, sys

def scanHost(ip, startPort, endPort):
    print(f'\n[-] Starting TCP port scan on host {ip}')
    tcp_scan(ip, startPort, endPort)
    print(f'\n[+] TCP scan on host {ip} complete\n')

def tcp_scan(ip, startPort, endPort):
    print("\n--------------|--------|-----------|----------|-----------")
    print("IP            |  PORT  |  PROTOCOL |  STATUS  |  SERVICE")
    print("--------------|--------|-----------|----------|-----------")
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                service = (socket.getservbyport(port, 'tcp'))
                print(f'{ip}  |   {port}   |    TCP    |   Open   |   {service}')
                print("--------------|--------|-----------|----------|-----------")
                tcp.close()
        except Exception:
            pass

if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:
        print('\nHelp: \n')
        print('Usage: ./port-scanner.py <IP address> <start port> <end port>')
        print('Example: ./port-scanner.py 31.146.68.230 1 65535\n')
    else:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])
        scanHost(network, startPort, endPort)
