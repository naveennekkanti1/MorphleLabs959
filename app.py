from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Set IST timezone
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    # Get system username
    username = os.getenv("USER", "codespace")

    # Get top command output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except subprocess.CalledProcessError as e:
        top_output = str(e)

    # HTML response
    response = f"""
    <html>
    <head><title>HTop Info</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Durga Naveen Nekkanti</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time:</strong> {server_time} IST</p>
        <pre><strong>Top output:</strong><br>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
