from flask import Flask, render_template
import logging

app = Flask(__name__)

@app.route('/')
def index():
    with open('honeypot.log', 'r') as log_file:
        logs = log_file.readlines()
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

