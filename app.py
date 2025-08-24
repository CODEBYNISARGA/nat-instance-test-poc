# app.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def check_nat():
    try:
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        return f"✅ NAT connectivity working! Public IP seen: {resp.json()['ip']}"
    except Exception as e:
        return f"❌ Failed to reach internet: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
