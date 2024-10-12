import nmap
import matplotlib.pyplot as plt
import time

# Function to scan network for active hosts and open ports
def scan_network(subnet):
    scanner = nmap.PortScanner()
    
    # Perform the scan
    print(f"Scanning the network: {subnet}")
    scanner.scan(hosts=subnet, arguments='-sn')  # Ping scan for host discovery

    active_hosts = []
    for host in scanner.all_hosts():
        if scanner[host].state() == "up":
            print(f"{host} is active")
            active_hosts.append(host)
    
    # Port scanning
    open_ports = {}
    scan_times = []
    for host in active_hosts:
        print(f"\nScanning open ports for {host}...")
        start_time = time.time()
        scanner.scan(host, arguments='-p 1-1024')  # Scan ports 1-1024
        end_time = time.time()
        
        scan_duration = end_time - start_time
        scan_times.append(scan_duration)  # Store scan time
        
        open_ports[host] = []
        
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                if scanner[host][proto][port]['state'] == 'open':
                    open_ports[host].append(port)
                    print(f"Port {port} is open on {host}")
    
    return active_hosts, open_ports, scan_times

# Get the target subnet to scan
target = input('Enter the subnet to be scanned (e.g., 192.168.1.0/24): ')
active_hosts, open_ports, scan_times = scan_network(target)

# Visualization
plt.figure(figsize=(12, 6))

# Plot open ports
plt.subplot(1, 2, 1)
for host, ports in open_ports.items():
    plt.scatter(ports, [host] * len(ports), label=host)
plt.title('Open Ports')
plt.xlabel('Port Number')
plt.ylabel('Host')
plt.legend(loc='upper right')

# Bar plot for scan times
plt.subplot(1, 2, 2)
plt.bar(active_hosts, scan_times, color='blue')  # Use blue bars
plt.title('Scan Times for Each Host')
plt.xlabel('Host')
plt.ylabel('Time (seconds)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

plt.tight_layout()
plt.show()
