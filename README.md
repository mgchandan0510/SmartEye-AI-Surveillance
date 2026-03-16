# SmartEye – AI Surveillance System

SmartEye is an **AI-powered surveillance system** designed for real-time intrusion detection using edge AI. The system captures live video through a camera, detects humans using a **YOLOv8 deep learning model**, and automatically sends alerts through a **Telegram bot**.  

It also provides a **web-based monitoring dashboard** to view the live camera feed, system logs, and recent alerts.

The project is designed to run on **low-cost edge devices like Raspberry Pi**, enabling real-time monitoring without relying on cloud services.

---

# Features

• Real-time human detection using YOLOv8  
• Edge AI inference running locally on Raspberry Pi  
• Instant Telegram alerts with captured image  
• Web dashboard for monitoring system status  
• Live camera feed streaming  
• Automatic event logging  
• Low-latency detection optimized for edge devices  

---

# Hardware Prototype

## SmartEye Enclosure

![SmartEye Outer Body](Outer%20Body.jfif)

A custom 3D-printed enclosure designed to house the SmartEye surveillance system with a front-facing camera module.

---

## Internal Hardware Setup

![SmartEye Internal Setup](Inner%20body.jfif)

The internal hardware architecture includes:

- Raspberry Pi (Edge AI processing)
- USB Camera Module
- Arduino Nano (sensor interfacing)
- Radar Motion Sensor
- Cooling Fan
- Power and communication connections

---

# System Architecture

The SmartEye system follows a layered architecture:
Camera Module
↓
Edge AI Processing (YOLOv8)
↓
Intrusion Detection Logic
↓
Alert Generation
↓
Telegram Notification
↓
Web Dashboard Monitoring


---

# Technologies Used

**Programming**
- Python

**AI / Computer Vision**
- YOLOv8
- OpenCV

**Backend**
- Flask

**Hardware**
- Raspberry Pi
- Arduino Nano
- USB Camera
- Radar Motion Sensor

**Communication**
- Telegram Bot API

---

# System Demonstration

## SmartEye System Mechanism

[▶ Watch Mechanism Video](SmartEye%20Mechanism.mp4)

This video demonstrates the internal working of the SmartEye system and hardware integration.

---

## Live Detection Demo

[▶ Watch System Demo](DEMO.mp4)

A real-time demonstration showing:

• Human detection  
• Alert triggering  
• Live monitoring dashboard  

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/smarteye-ai-surveillance.git
cd smarteye-ai-surveillance

