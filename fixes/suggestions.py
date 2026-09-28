def generate_fix_suggestions(report):
    fixes = []

    conn = report.get("connectivity", {})
    dns = report.get("dns", {})
    ipcfg = report.get("ip_config", {})
    ports = report.get("ports", {})

    # Connectivity-based suggestions
    if not conn.get("external_site", {}).get("success", False):
        fixes.append("Internet unreachable. Check router/modem and verify gateway connectivity.")
        fixes.append("Restart network adapter or reconnect to Wi-Fi/Ethernet.")

    if not conn.get("dns_google", {}).get("success", False):
        fixes.append("DNS may be failing. Switch DNS to 8.8.8.8 or 1.1.1.1.")
        fixes.append("Run: ipconfig /flushdns")

    # DNS-based suggestions
    if not dns.get("github", {}).get("success", True):
        fixes.append("DNS resolution failed. Verify DNS server settings or restart router.")

    # IP config suggestions
    if not ipcfg.get("success", True):
        fixes.append("Unable to read IP configuration. Ensure network adapter is enabled.")
    else:
        fixes.append("Check for APIPA (169.254.x.x) or missing gateway in IP configuration.")
        fixes.append("If APIPA detected, renew DHCP lease: ipconfig /release && ipconfig /renew")

    # Port-based suggestions
    if not ports.get("https", {}).get("open", True):
        fixes.append("HTTPS port blocked. Check firewall, VPN, or proxy settings.")

    if not ports.get("dns", {}).get("open", True):
        fixes.append("DNS port blocked. Firewall or ISP may be interfering.")

    # If nothing is wrong
    if not fixes:
        fixes.append("No issues detected. Network appears healthy.")

    return fixes
