import subprocess
import re
from collections import Counter
def app():
    while True:
        user_input = input("How many minutes ago do you want to check?")
        if user_input.isdigit():
            break
        print("write a number")
    try:
        logs = subprocess.check_output(["journalctl", "-u", "sshd", "--since", f"{user_input} minutes ago"], text=True)
        if logs.strip():
            print("=== LOGI SSH ===")
            print(logs)
            failed = []
            for line in logs.split("\n"):
                if "Failed password" in line:
                    failed.append(line)
            print(f"\033[91m=== FAILED LOGS ===\33[0m")
            for f in failed:
                print(f)
            ips = []
            for line in failed:
                match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
                if match:
                    ips.append(match.group(0))
            print()
            print(f"\033[92m=== IPS ===\33[0m")
            counter = Counter(ips)
            for ip, count in counter.items():
                if count >= 3:
                    print()
                    print(f"\033[91m=== [ALERT] Possible brute force from {ip} ({count} attempts) ===\33[0m")
        else:
            print(f"No new SSH log entries found in the last {user_input} minutes.")
    except subprocess.CalledProcessError:
        print("RUN IT AS A ROOT")
if __name__ == "__main__":
    app()
