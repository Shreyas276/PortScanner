🔍 Python PortScanner

A lightweight Python tool to scan open ports on one or multiple targets. Built using the `socket` and `termcolor` libraries, this script is CLI-based and beginner-friendly.

📦 Features

- Scan **single or multiple targets**
- Specify the number of ports to scan
- Clean, color-coded output using `termcolor`
- Skips closed ports silently

📸 Screenshot

[+] Starting Scan For 192.168.1.1
[+] Port Opened: 22
[+] Port Opened: 80

🚀 How to Run

1. Install dependencies:

   pip install termcolor

2. Run the script:

   python3 portscanner.py

🧑💻 Input Format

Enter multiple targets separated by `;`
You’ll be prompted for how many ports to scan (starts from port 1)

Example:

Enter Targets To Scan(Split Them by ;): 192.168.1.1;192.168.1.2
Enter How Many Ports To Be Scanned: 100

📁 Project Structure

📁 tools/
├── portscanner.py

⚠ Disclaimer

This tool is meant for **educational and authorized use only**. Never scan IPs you don’t own or have permission to test.

🪪 Author

Made with ❤ by [Shreyas276](https://github.com/Shreyas276)
