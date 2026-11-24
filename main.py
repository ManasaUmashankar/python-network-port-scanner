from src.scanner import (
    scan_ports,
    get_service_name,
    validate_port_range,
    validate_ip_address
)

print("=" * 45)
print("       PYTHON NETWORK PORT SCANNER")
print("=" * 45)

host = input("\nEnter target IP address: ").strip()

if not validate_ip_address(host):
    print("Invalid IP address.")
else:
    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if not validate_port_range(start_port, end_port):
            print("Invalid port range. Use ports between 1 and 65535.")
        else:
            print(f"\nScanning {host}...")
            print(f"Port range: {start_port}-{end_port}\n")

            open_ports = scan_ports(host, start_port, end_port)

            if open_ports:
                print("Open ports found:\n")

                for port in open_ports:
                    service = get_service_name(port)
                    print(
                        f"Port: {port} | "
                        f"Service: {service} | Status: OPEN"
                    )
            else:
                print("No open ports found.")

            print("\nScan completed.")

    except ValueError:
        print("Please enter valid numeric port numbers.")