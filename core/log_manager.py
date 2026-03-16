from collections import deque
from datetime import datetime
import threading

class LogManager:
    def __init__(self):
        self.logs = deque(maxlen=50) # Keep last 50 lines
        self.lock = threading.Lock()

    def log(self, message):
        """Adds a timestamped message to the log buffer"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {message}"
        
        # Print to terminal (for systemd logs)
        print(entry)
        
        # Add to memory (for Web Dashboard)
        with self.lock:
            self.logs.appendleft(entry) # Newest first

    def get_logs(self):
        """Returns list of logs for the web server"""
        with self.lock:
            return list(self.logs)

# Global instance to be used by all modules
logger = LogManager()
