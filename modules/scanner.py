import socket 

def scan_ports(target):
    results = "[*] Scanning ports...\n"

    ports = [21, 22, 23, 25, 80, 110, 143, 443, 445, 1433, 3306, 3389, 5432]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((target, port))
            results += f"[+] {port} is OPEN\n"
        except:
            results += f"[-] {port} is closed or filtered\n"
        finally:
            sock.close()
    
    return results
