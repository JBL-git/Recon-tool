import socket

def lookup(target):
    try:
        ip = socket.gethostbyname(target)
        return f"[+] IP Address: {ip}\n"
    except Exception:
        return "[-] Could not resolve target\n"