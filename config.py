import os
import cv2

# --- PATHS ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPTURE_DIR = os.path.join(BASE_DIR, "captures")
MODEL_PATH = "yolov8n.pt"

# --- CAMERA ---
CAMERA_INDEX = 0  # Camera at index 1
RESOLUTION = (320, 240)  # VERY LOW for instant detection

# --- FIXED: ROTATION REMOVED ---
ROTATE_FRAME = None  

# --- AI & LOGIC ---
CONF_THRESHOLD = 0.40          # LOWER for faster human detection
IMG_SZ = 160                   # VERY SMALL for ultra-fast inference
DETECT_EVERY_N_FRAMES = 1      # Process EVERY frame
SMOOTH_WINDOW = 2              # Small window for fast alerts
HUMAN_CONFIRM_COUNT = 1        # Alert on FIRST detection
RESET_ON_NO_HUMAN_CHECKS = 10  # Reset after 10 frames without human

# --- CLASS MAPPING ---
HUMAN_NAMES = {"person"}
ANIMAL_NAMES = {"dog", "cat", "horse", "sheep", "cow", "bear", "zebra"}
VEHICLE_NAMES = {"car", "truck", "bus", "bicycle", "motorcycle"}    

# --- NEW: Telegram Settings ---
TELEGRAM_TOKEN = "your token"
TELEGRAM_CHAT_ID = "your chatid"

# --- PERFORMANCE OPTIMIZATIONS ---
USE_MOTION_DETECTION = False    # Disabled for instant detection
DETECTION_CACHE_SIZE = 20       # Small cache
MIN_DETECTION_INTERVAL = 0.1    # Very short interval (100ms)
ALERT_COOLDOWN = 5              # 5 seconds between alerts (much shorter)
