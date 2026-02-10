from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    return f"Today's date is: {today} <br>Current time is: {current_time}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
