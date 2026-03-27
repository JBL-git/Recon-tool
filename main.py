import sys
from modules import scanner, dns, utils

if len(sys.argv) !=2:
    print("Usage: python3 main.py <target>")
    sys.exit(1)

target = sys.argv[1]
print(f"[+] Initiating recon on {target}\n")

dns_result = dns.lookup(target)
scan_result = scanner.scan_ports(target)

print(dns_result)
print(scan_result)




