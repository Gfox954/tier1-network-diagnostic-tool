import subprocess

def get_ipconfig():
    try:
        result = subprocess.run(
            ["ipconfig", "/all"],
            capture_output=True,
            text=True
        )
        return {"success": True, "output": result.stdout}
    except Exception as e:
        return {"success": False, "error": str(e)}

def run_ip_config_checks():
    data = get_ipconfig()
    # Later we will parse this output to detect APIPA, missing gateway, DHCP issues, etc.
    return data
