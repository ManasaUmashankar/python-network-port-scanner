# Python Network Port Scanner

A beginner-friendly TCP port scanner built using Python's socket programming capabilities. It checks a specified range of ports on an IPv4 address and identifies ports that accept TCP connections.

## Features

- IPv4 address validation
- TCP port scanning using Python sockets
- Customizable port ranges
- Open port detection
- Basic service-name lookup
- Scan progress display
- Port-range validation (maximum 1,000 ports per scan)
- Automated tests using pytest

## Project Structure

```text
python-network-port-scanner/
├── src/
│   └── scanner.py
├── tests/
│   └── test_scanner.py
├── main.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or later
- pytest (for running tests)

No external libraries are required for the scanner itself.

## Installation

Clone the repository:

```bash
git clone https://github.com/ManasaUmashankar/python-network-port-scanner.git
```

Navigate into the project:

```bash
cd python-network-port-scanner
```

Install pytest:

```bash
python -m pip install pytest
```

## Usage

Run the scanner:

```bash
python main.py
```

Enter the requested information:

```text
Enter target IP address: 127.0.0.1
Enter starting port: 80
Enter ending port: 100
```

The scanner displays open ports and their conventional service-name mappings.

## Run Tests

```bash
python -m pytest -v
```

## Concepts Practiced

- Python socket programming
- TCP connections
- IP address validation
- Port-range validation
- Exception handling
- Functions and loops
- Automated testing with pytest

## Limitations

- Supports IPv4 addresses only.
- Scans TCP ports only.
- Scans a maximum of 1,000 ports per execution.
- Service names are conventional port mappings, not verified application identities.

## Responsible Use

Use this tool only on systems you own or have explicit permission to test. Unauthorized port scanning may violate policies or laws.
