import socket


def scan_port(hst, prt):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the timeout to 1 second
    s.settimeout(1)

    # Try to connect to the port
    result = s.connect_ex((hst, prt))

    # If the connection was successful, the port is open
    if result == 0:
        print(f"Port {prt} is open")
    else:
        print(f"Port {prt} is not open")

    # Close the socket
    s.close()


# Define the host and the range of ports to scan
host = "google.com"
start_port = 1
end_port = 65535

# Scan all the ports in the specified range
for port in range(start_port, end_port+1):
    scan_port(host, port)
