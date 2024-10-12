# Network Scanner with Visualization

This Python script scans a specified network subnet for active hosts and open ports, then presents the results in a visual format.

## Requirements

- Python 3
- nmap - Install using `pip install nmap` (may require administrator privileges)
- matplotlib - Install using `pip install matplotlib`

## Instructions

1. Save the code as `network_scanner.py`.
2. Run the script from your terminal: `python network_scanner.py`
3. Enter the subnet to be scanned in the format `XXX.XXX.XXX.0/XX` (e.g., `192.168.1.0/24`).

## Output

The script will display a visualization with two subplots:
- **Open Ports**: A scatter plot showing open ports on each identified host.
- **Scan Times**: A bar graph illustrating the time taken to scan each host.

## Explanation

### `scan_network` function:
- Takes a subnet address as input.
- Uses `nmap.PortScanner` to perform a ping scan for host discovery.
- Stores active hosts in a list.
- Iterates through active hosts, scans ports 1-1024 with `nmap`, and records open ports and scan times.
- Returns lists of active hosts, open ports, and scan times.

### Main program:
1. Prompts the user for the subnet to scan.
2. Calls `scan_network` and stores the results.
3. Creates a visualization using `matplotlib.pyplot`:
   - Scatter plot for open ports.
   - Bar plot for scan times per host.
4. Displays the visualization.

## Additional Notes

- Running a network scan without permission may be illegal. Use this script ethically and responsibly.
- Consider customizing the port range scanned based on your specific needs.
- You can adjust the visualization layout and styling using `matplotlib` options.
