import threading
import sys
import time
from camera_core import CameraCore
from web_server import start_server
from log_manager import logger

def main():
    logger.log("System Initializing...")
    
    # Initialize Camera
    cam = CameraCore()
    
    # Run Camera Loop in background thread
    cam_thread = threading.Thread(target=cam.run, daemon=True)
    cam_thread.start()

    logger.log(f"Web Server Starting on 0.0.0.0:5000")
    
    try:
        # Blocks here running the web server
        start_server(cam)
    except KeyboardInterrupt:
        logger.log("Stopping System...")
        cam.is_running = False
        sys.exit(0)

if __name__ == "__main__":
    main()
