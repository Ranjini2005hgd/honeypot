mport socket
import logging
import threading
from collections import defaultdict
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(a>

connection_count = defaultdict(int)

def send_alert(ip):
    msg = MIMEText(f"Alert! Connection from suspicious IP: {ip}")
    msg['Subject'] = 'Honeypot Alert'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'your_email@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

def handle_connection(conn, addr):
    global connection_count
    with conn:
        connection_count[addr[0]] += 1
        print(f"Connection from {addr} (Total: {connection_count[addr[0]]})")
        logging.info(f"Connection from {addr} (Total: {connection_count[addr>
        conn.sendall(b"Welcome to the honeypot!\n")
        data = conn.recv(1024)
        if data:
            print(f"Received data: {data.decode()}")
            logging.info(f"Received data from {addr}: {data.decode()}")
            if connection_count[addr[0]] > 5:  # Example condition for alert>
                send_alert(addr[0])

def start_honeypot(host='0.0.0.0', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Honeypot listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
thread = threading.Thread(target=handle_connection, args=(conn, >
            thread.start()

if __name__ == "__main__":
    start_honeypot()


