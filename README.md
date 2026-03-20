# 🛡️ LogAuthQuickScript

Lightweight Python tool for detecting suspicious SSH authentication activity from system logs.

## 📝 Overview
**LogAuthQuickScript** analyzes SSH authentication logs and highlights suspicious behavior such as repeated failed login attempts from the same IP address. It is designed as a simple and fast command-line utility for basic intrusion detection.

## ✨ Key Capabilities
* **Monitor** SSH authentication logs via `journalctl`.
* **Detect** failed login attempts in real-time.
* **Extract** and analyze source IP addresses using Regex.
* **Identify** potential brute-force activity automatically.
* **Provide** readable, color-coded terminal output.

## ⚙️ How It Works
The script retrieves recent SSH logs and processes them in four steps:
1. **Collect** logs from a specified time window using `journalctl`.
2. **Filter** failed authentication attempts (specifically "Failed password" strings).
3. **Extract** IP addresses using pattern matching (`re`).
4. **Count** attempts per IP and trigger alerts if a threshold (3+ attempts) is met.

## 🚀 Usage
To run the script, use the following command:

```bash
python SSHLogAuthQuickScript.py
````

*Enter the number of minutes to analyze when prompted.*

### Example Output

```text
=== SSH LOGS ===

=== FAILED LOGS ===
Failed password for user from 192.168.1.10
Failed password for user from 192.168.1.10
Failed password for user from 192.168.1.10

=== IPS ===

[ALERT] Possible brute force from 192.168.1.10 (3 attempts)
```

## 🛠️ Requirements

  * **Python 3.x**
  * **Linux system** with `systemd` (e.g., Arch Linux, Debian, Ubuntu)
  * **Access** to `journalctl` (Root/Sudo permissions)

**Run with elevated privileges (Required):**

```bash
sudo python SSHLogAuthQuickScript.py
```

## 🚧 Project Status

**Active development** — features are being added incrementally.

### 🗺️ Roadmap

  * [ ] **Real-time monitoring:** Add a live "tail" mode for continuous log watching.
  * [ ] **Alert export:** Support for JSON or plain text file logging.
  * [ ] **Enhanced CLI:** Better formatting and argument parsing.
  * [ ] **Extended logic:** GeoIP support to see where attackers are coming from.

## ⚠️ Notes

  * This project is intended for **educational purposes** and basic security analysis.
  * Use only in environments you own or are authorized to monitor.
