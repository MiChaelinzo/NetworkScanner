import socket

# Create a socket object
s = socket.socket()

# Define the target host and port
host = 'localhost'
port = 8080

# Connect to the target host and port
s.connect((host, port))

# Send a request to the target host
s.send('GET / HTTP/1.1\r\n\r\n')

# Receive the response from the target host
response = s.recv(1024)

# Print the response
print(response)

# Close the socket connection
s.close()
