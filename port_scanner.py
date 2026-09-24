#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def scan_port(target_ip, port, timeout=1):

    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Attempt to connect
        result = sock.connect_ex((target_ip, port))
        sock.close()

        # If connect_ex returns 0, the port is open
        return result == 0
    except socket.gaierror:
        print(f"Error: Invalid IP address or hostname '{target_ip}'")
        sys.exit(1)
    except socket.error as e:
        print(f"Socket error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def validate_ip(ip):

    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def validate_port_range(start_port, end_port):

    return (1 <= start_port <= 65535 and
            1 <= end_port <= 65535 and
            start_port <= end_port)

def main():
    """Main function to run the port scanner."""
    print("=" * 50)
    print("Simple TCP Port Scanner")
    print("=" * 50)

    # Get target IP
    while True:
        target_ip = input("\nEnter target IP address: ").strip()
        if validate_ip(target_ip):
            break
        print("Invalid IP address. Please enter a valid IPv4 address (e.g., 192.168.1.1)")

    # Get port range
    while True:
        try:
            port_input = input("Enter port range (e.g., 1-1000) or single port: ").strip()
            if '-' in port_input:
                start_str, end_str = port_input.split('-', 1)
                start_port = int(start_str)
                end_port = int(end_str)
            else:
                start_port = end_port = int(port_input)

            if validate_port_range(start_port, end_port):
                break
            else:
                print("Invalid port range. Ports must be between 1-65535 and start <= end")
        except ValueError:
            print("Please enter valid port numbers")

    # Optional: timeout
    timeout_input = input("Enter timeout in seconds (default: 1): ").strip()
    try:
        timeout = float(timeout_input) if timeout_input else 1.0
        if timeout <= 0:
            print("Timeout must be positive, using default 1 second")
            timeout = 1.0
    except ValueError:
        print("Invalid timeout, using default 1 second")
        timeout = 1.0

    print("\n" + "=" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Timeout: {timeout} second(s)")
    print("=" * 50)

    start_time = datetime.now()
    open_ports = []

    try:
        # Scan each port in the range
        for port in range(start_port, end_port + 1):
            if scan_port(target_ip, port, timeout):
                print(f"Port {port}: OPEN")
                open_ports.append(port)
            # Optional: show progress for large ranges
            elif (port - start_port) % 100 == 0 and port > start_port:
                print(f"Scanned up to port {port}...")
    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
    except Exception as e:
        print(f"\n\nError during scan: {e}")

    end_time = datetime.now()
    scan_duration = end_time - start_time

    # Summary
    print("\n" + "=" * 50)
    print("Scan Summary")
    print("=" * 50)
    print(f"Target: {target_ip}")
    print(f"Ports scanned: {start_port}-{end_port} ({(end_port - start_port + 1)} ports)")
    print(f"Open ports found: {len(open_ports)}")
    if open_ports:
        print("Open ports:", ", ".join(map(str, sorted(open_ports))))
    print(f"Scan duration: {scan_duration}")
    print("=" * 50)

if __name__ == "__main__":
    main()
