import socket

def resolve(host):
    try:
        ip = socket.gethostbyname(host)
        return {"host": host, "resolved_ip": ip, "success": True}
    except Exception as e:
        return {"host": host, "success": False, "error": str(e)}

def run_dns_tests():
    tests = {}
    tests["github"] = resolve("github.com")
    tests["google"] = resolve("google.com")
    tests["microsoft"] = resolve("microsoft.com")
    return tests
