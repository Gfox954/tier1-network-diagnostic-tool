import subprocess

def ping(host):
    try:
        result = subprocess.run(
            ["ping", "-n", "3", host],
            capture_output=True,
            text=True
        )
        success = (result.returncode == 0)
        return {
            "host": host,
            "success": success,
            "output": result.stdout
        }
    except Exception as e:
        return {
            "host": host,
            "success": False,
            "error": str(e)
        }

def run_ping_tests():
    tests = {}
    tests["loopback"] = ping("127.0.0.1")
    tests["gateway"] = ping("192.168.0.1")  # adjust if your gateway is different
    tests["dns_google"] = ping("8.8.8.8")
    tests["external_site"] = ping("github.com")
    return tests
