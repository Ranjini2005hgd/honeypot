# Honeypot Setup with Cowrie

This repository demonstrates setting up a honeypot using Cowrie to log and monitor malicious activity.

## Features
- SSH and Telnet emulation.
- Logs all interactions for analysis.
- Customizable configuration.

## Installation
1. Clone this repository:
git clone https://github.com/your-username/honeypot-setup.git cd honeypot-setup
2. Run the setup script:
bash setup.sh
3. Start the honeypot:
bin/cowrie start
4. Stop the honeypot:
bin/cowrie stop

## Logs
Logs are stored in `var/log/cowrie`.

## Scripts
- Use `scripts/analyze_logs.py` to analyze logs for insights.

## License
This project is licensed under the MIT License.
