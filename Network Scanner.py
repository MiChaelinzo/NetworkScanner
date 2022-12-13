import socket

def scan_network(network):
  # Create a socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Set a timeout so the socket does not block indefinitely
  s.settimeout(0.5)

  # Scan the network for open ports
  for port in range(1, 1024):
    try:
      # Try to connect to the port
      s.connect((network, port))

      # If the connection succeeds, the port is open
      print(f"Port {port} is open")
    except:
      # If the connection fails, the port is closed or filtered
      pass

# Scan the local network
scan_network("192.168.0.1")
