import nmap

# initialize nmap scanner
nm_scan = nmap.PortScanner()

# scan localhost for ports in range 21-443
nm_scan.scan('localhost', '21-443')

# get all scan results
scan_results = nm_scan.all_hosts()

# loop through scan results
for host in scan_results:
  print('------------------')
  print('Host : %s (%s)' % (host, nm_scan[host].hostname()))
  print('State : %s' % nm_scan[host].state())
 
  # loop through all protocols
  for proto in nm_scan[host].all_protocols():
    print('----------')
    print('Protocol : %s' % proto)
    
    # get all ports for protocol
    ports = nm_scan[host][proto].keys()
    
    # sort ports in numerical order
    sorted_ports = sorted(ports)
    
    # loop through all ports
    for port in sorted_ports:
      print('port : %s\tstate : %s' % (port, nm_scan[host][proto][port]['state']))
