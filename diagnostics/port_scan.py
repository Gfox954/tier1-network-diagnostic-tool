import socket

COMMON_PORTS = {
    "http": 80,
    "https": 443,
    "dns": 53,
    "ssh": 22,
    "rdp": 3389
}

def check_port(host, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        s.close()
        return {"host": host, "port": port, "open": True}
    except Exception:
        return {"host": host, "port": port, "open": False}

def run_port_scan():
    results = {}
    for name, port in COMMON_PORTS.items():
        results[name] = check_port("8.8.8.8", port)  # Google DNS as a stable test host
    return results
