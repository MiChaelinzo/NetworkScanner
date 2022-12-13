import nmap
import socket
from collections import defaultdict

# initialize nmap scanner
nm_scan = nmap.PortScanner()

# scan local network for ports in range 1-65535
nm_scan.scan(hosts='192.168.0.0/24', ports='1-65535')

# get all scan results
scan_results = nm_scan.all_hosts()

# create dictionary to store vulnerability information
vuln_dict = defaultdict(list)

# loop through scan results
for host in scan_results:
  # get hostname and IP address
  hostname = nm_scan[host].hostname()
  ip_address = socket.gethostbyname(hostname)

  # loop through all protocols
  for proto in nm_scan[host].all_protocols():
    # get all open ports for protocol
    open_ports = nm_scan[host][proto]['tcp'].keys()

    # loop through open ports and check for vulnerabilities
    for port in open_ports:
      # check if port is vulnerable
      if nm_scan[host].has_vuln(port):
        # get vulnerability information
        vuln_info = nm_scan[host].vuln_info(port)
        
        # add vulnerability information to dictionary
        vuln_dict[hostname].append((ip_address, port, vuln_info))

# print vulnerability information
for host, info in vuln_dict.items():
  print('------------------')
  print('Hostname : %s' % host)
  for vuln in info:
    print('IP address : %s' % vuln[0])
    print('Port : %s' % vuln[1])
    print('Vulnerability : %s' % vuln[2])


