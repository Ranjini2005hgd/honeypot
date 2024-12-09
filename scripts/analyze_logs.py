import json

LOG_FILE = "cowrie/var/log/cowrie/cowrie.json"

def analyze_logs():
    try:
        with open(LOG_FILE, 'r') as log_file:
            for line in log_file:
                log = json.loads(line.strip())
                print(f"Time: {log.get('timestamp')}, Event: {log.get('eventid')}, IP: {log.get('src_ip')}")
    except FileNotFoundError:
        print(f"Log file not found: {LOG_FILE}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    analyze_logs()
