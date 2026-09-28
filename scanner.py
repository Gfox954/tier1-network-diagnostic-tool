import json
from diagnostics.ping_test import run_ping_tests
from diagnostics.dns_test import run_dns_tests
from diagnostics.ip_config import run_ip_config_checks
from diagnostics.port_scan import run_port_scan
from fixes.suggestions import generate_fix_suggestions

def main():
    report = {}

    # 1. Connectivity (ping)
    report["connectivity"] = run_ping_tests()

    # 2. DNS
    report["dns"] = run_dns_tests()

    # 3. IP config
    report["ip_config"] = run_ip_config_checks()

    # 4. Port scan
    report["ports"] = run_port_scan()

    # 5. Fix suggestions
    report["fixes"] = generate_fix_suggestions(report)

    # 6. Save JSON
    with open("reports/network_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Network diagnostic complete. Report saved to reports/network_report.json")

if __name__ == "__main__":
    main()
