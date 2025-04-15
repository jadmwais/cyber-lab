import socket
import time

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP (e.g., 127.0.0.1): ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    
    start_time = time.time()
    scan_ports(target, start, end)
    end_time = time.time()
    
    print(f"\nScan completed in {end_time - start_time:.2f} seconds.")
