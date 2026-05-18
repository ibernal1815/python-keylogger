# python-keylogger

a modular Python keylogger with AES-encrypted keystroke transmission to a Flask-based C2 server. built to understand how endpoint exfiltration actually works, not just what it looks like in a diagram.

## background / why i built this

exfiltration is one of the last stages in the kill chain and one of the hardest to detect when it is done quietly. i wanted to build the tooling myself so i understood what the traffic looks like, how the data gets captured and transmitted, and where the detection opportunities are for a defender.

this is not a deployment tool. it runs in a sandboxed VM, it has a local test mode, and the whole point is to understand the technique so i can build better detections against it.

tested only on self-owned systems in isolated virtualized environments on macOS and Linux.

## what it does

captures keystrokes cross-platform using pynput and transmits them to a Flask-based C2 server over HTTP POST. logs are AES-encrypted before transmission so the data is not sitting in plaintext on the wire. optional screenshot capture grabs the active window at configurable intervals.

the project is split into a keylogger module, a C2 server, and a scripts folder with a local test mode and a simulated stager for testing the full payload drop flow without live deployment.

## project layout

```
python-keylogger/
├── keylogger/
│   ├── logger.py          # keylogging logic
│   ├── config.py          # configurable options
│   └── utils.py           # encryption and screenshots
├── c2_server/
│   ├── server.py          # Flask C2 endpoint
│   └── logs/              # received log storage
├── scripts/
│   ├── run_local_test.py  # safe sandboxed test mode
│   └── client_stager.py   # simulated payload drop
├── screenshots/
└── .gitignore
```

## setup

```bash
git clone https://github.com/ibernal1815/python-keylogger.git
cd python-keylogger
pip install -r requirements.txt
```

run the C2 server first:

```bash
python c2_server/server.py
```

run the local test:

```bash
python scripts/run_local_test.py
```

## detection notes

running this in a lab surfaces several detection opportunities worth noting. pynput registers a global input hook which triggers process baseline anomalies in Sysmon. outbound HTTP POST traffic to a non-browser process is a strong network indicator. AES key material in memory is visible under a debugger if the process is caught mid-execution.

## stack

Python 3 · pynput · Flask · PyCryptodome · requests
