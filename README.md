# 🛡️ Python Keylogger with Remote C2 Server

This project demonstrates a modular Python keylogger with optional screenshot capture and encrypted keystroke transmission to a Flask-based C2 server. It was developed strictly for educational, ethical, and red-team lab use.

---

## 🔧 Features

- ✅ Cross-platform keylogging via `pynput`
- 🌐 Secure client-server communication via HTTP POST
- 🔐 Optional AES-encrypted logs
- 🖼️ Optional screenshot capture of active window
- ⚙️ Modular config system and sandbox test script

---

## 🧠 Purpose

This project is intended to demonstrate how endpoint data exfiltration can occur in adversarial simulations, helping security professionals develop better detection and mitigation strategies.

**Tested only on self-owned systems in virtualized environments (macOS and Linux).**

---

## 📁 Project Structure

python-keylogger/
├── keylogger/
│ ├── logger.py # Keylogging logic
│ ├── config.py # Configurable options
│ └── utils.py # Encryption, screenshots
├── c2_server/
│ ├── server.py # Flask server endpoint
│ └── logs/ # Log file storage
├── scripts/
│ ├── run_local_test.py # Safe local test mode
│ └── client_stager.py # Simulated payload drop
├── screenshots/ # Screenshots from demo
├── .gitignore
└── README.md
