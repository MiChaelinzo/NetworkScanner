# Import the nmap library
import nmap

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Scan the network for hosts
nm.scan(hosts='192.168.1.0/24', arguments='-sV')

# Print the scan results
for host in nm.all_hosts():
    print('Host: %s (%s)' % (host, nm[host].hostname()))
    print('State: %s' % nm[host].state())

    for protocol in nm[host].all_protocols():
        print('Protocol: %s' % protocol)

        port_info = nm[host][protocol].keys()
        for port in port_info:
            print('port: %s\tstate: %s' % (port, nm[host][protocol][port]['state']))
