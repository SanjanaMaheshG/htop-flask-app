from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system details
    name = "Sanjana Mahesh Gadakari"  # Your full name
    username = os.getenv('USER', 'Unknown')  # Get system username
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

    # Run `top` command and capture output
    top_output = subprocess.getoutput('top -b -n 1 | head -10')

    # Create the HTML output
    html_output = f"""
    <html>
        <head><title>HTOP</title></head>
        <body>
            <h1>HTOP Endpoint</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    
    return html_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
