from flask import Flask, render_template, Response, jsonify
import os
from config import CAPTURE_DIR
from log_manager import logger

app = Flask(__name__, template_folder="../templates")
camera_instance = None 

def gen_frames():
    while True:
        if camera_instance:
            frame = camera_instance.get_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    captures = []
    if os.path.exists(CAPTURE_DIR):
        captures = sorted(os.listdir(CAPTURE_DIR), reverse=True)[:10] # Show last 10
    return render_template('index.html', captures=captures)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# --- NEW: Log API ---
@app.route('/api/logs')
def get_logs():
    return jsonify(logger.get_logs())

def start_server(cam_obj):
    global camera_instance
    camera_instance = cam_obj
    # 0.0.0.0 means it binds to ALL IPs (including your hotspot IP 10.190.x.x)
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
