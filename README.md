# Port Scanner CLI

A simple command-line application to check open or closed ports on a given host. This tool uses multithreading to perform fast scans across multiple ports or port ranges.

## Features
- Check if ports are open or closed on a given host.
- Supports scanning individual ports, comma-separated ports, and ranges of ports.
- Multithreaded to speed up the scanning process.

## Installation

Clone or download the repository, and use the provided Python file `main.py`.

```bash
git clone https://github.com/LeoTz/Port-Scanner-CLI-Tool
cd Port-Scanner-CLI-Tool
```

## Usage

You can run the port scanner with the following command:

```bash
python main.py <host_name> -p <port_range>
```

Where:
- `<host_name>`: The name or IP address of the host you want to scan.
- `-p <port_range>`: A list or range of ports to scan. You can specify:
  - A comma-separated list of ports: `80,443,8080`
  - A range of ports: `20-80`
 
### Example Usage

Scan a single port:

```bash
python main.py example.com -p 80
```

Scan multiple ports:

```bash
python main.py example.com -p 80,443,22
```

Scan a range of ports:

```bash
python main.py example.com -p 20-80
```

## Version

You can check the current version of the application with the following command:

```bash
python main.py --version
```

