
import socket
import ipaddress


def validate_ip_address(host):
    try:
        ip = ipaddress.ip_address(host)
        return isinstance(ip, ipaddress.IPv4Address)
    except ValueError:
        return False


def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(2)
            result = client.connect_ex((host, port))
            return result == 0

    except socket.error:
        return False


def scan_ports(host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        print(f"Checking port {port}...")

        if check_port(host, port):
            open_ports.append(port)

    return open_ports


def get_service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "Unknown service"


def validate_port_range(start_port, end_port):
    if not isinstance(start_port, int) or not isinstance(end_port, int):
        return False

    if start_port < 1 or end_port > 65535:
        return False

    if start_port > end_port:
        return False

    if end_port - start_port + 1 > 1000:
        return False

    return True