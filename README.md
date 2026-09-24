# Simple TCP Port Scanner
- A simple and eays to use port scanner that checks for open ports on a target IPv4 address and provides summary of results

# Features
- Interactive CLI -- allows for guided prompts depending on the target
- IPv4 validation -- rejects malformed addresses before scanning
- Adjustable timeout -- can finetune for spped vs. accuracy
- Interruption -- allows for interruption with Ctrl+C

# Requirements
- Python 3.6+
- No third-party dependencies(uses only the Python standard library)

#Installation
- Clone the repository
```bash
git clone https://github.com/pimpmasterplayboy/port-scanner.git
cd port-scanner
```
- (Optional) Make the script executable
```bash
chmod +x port_scanner.py
```
- Run the scanner
```bash
python3 port_scanner.py
```
- Or if you make it executable:
```bash
./port-scanner.py
```

# Usage
- Very simple and is used the same as any other port scanner
- The scanner is able to run interactively so you simply enter the information which is asked of you
- Enter the target IP, Port range, Timeout

# Examples
- Single port scan:
```bash
Enter target IP address: 127.0.0.1
Enter port range (e.g., 1-1000) or single port: 22
Enter timeout in seconds (default: 1):
```
- Sample output:
```bash
==================================================
Scanning target: 192.168.1.1
Port range: 1-1000
Timeout: 1.0 second(s)
==================================================
Port 22: OPEN
Port 80: OPEN
Port 443: OPEN
Scanned up to port 101...
Scanned up to port 201...
...
==================================================
Scan Summary
==================================================
Target: 192.168.1.1
Ports scanned: 1-1000 (1000 ports)
Open ports found: 3
Open ports: 22, 80, 443
Scan duration: 0:00:42.318927
==================================================
```

# Limitations
- sequential scanning -- ports are scanned one at a time
- TCP only
- Full connect scan -- easily logged by the target host's services
- No service banner grabbing -- Only reports open/closed status
- IPv4 only
- There is still much room for future improvement and these are all things that could possibly be updated in the future


# Legal Disclamer
Use this tool responsibly. Port scanning a host you do not own or have explicit permission to scan may be illegal in many jurisdictions and is often a violation of acceptable-use policies and terms of service.

Only scan hosts you own (e.g., 127.0.0.1, your home network, or lab VMs).
Obtain written authorization before scanning third-party systems.
Follow all local, state, and federal laws.
Do not use this tool to scan public hosts, employer networks, or cloud services without permission.
The authors and contributors of this project are not responsible for any misuse or damage caused by this software. You assume all responsibility for your use of this tool.

# Acknowledgement
- this tool is obviously inspired by similar ones such as nmap or netcat, simplified and made for means of education and improvement

