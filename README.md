# 🤖 Ethan & E3N – AI Robot + Voice Assistant

**Ethan** is a sustainable AI robot developed from e-waste, showcasing IoT motion and speech interaction during the NAAC accreditation visit.  
**E3N (Ethan v3)** is a cross-platform intelligent voice assistant combining speech recognition, natural text-to-speech, and AI-powered dialogue via Pi.ai.

Together, these two projects demonstrate the fusion of **embedded hardware**, **AI software**, and **natural language interaction** built by Shivam Kumar (ECE, AEC).

---

## 📸 Project Demo

<p align="center">
  <img src="Public/IMG_20231203_172813 (1).jpg" alt="Ethan AI Robot" width="400"/>
</p>

> *Left: E3N Voice Assistant UI*  
> *Right: Ethan Robot on display during NAAC visit (Dec 4, 2023)*

---

## 🔧 Overview

| Project | Description |
|--------|-------------|
| 🧍‍♂️ **Ethan (Robot)** | A physical robot made from e-waste with speech-based interaction and IoT motion |
| 💬 **E3N (Voice Assistant)** | A software assistant with TTS, STT, and web-based AI integration via Pi.ai |
## 📁 Project Structure

F:\E3N\
├── 📁 Project Root
│   ├── 📄 ar.py                    # Audio Recognition & Pi.ai Integration
│   ├── 📄 communicate.py           # Edge TTS Communication Module
│   ├── 📄 update.py                # Video Playback & Media Handler
│   ├── 📄 README.md               # Project Documentation
│   └── 📄 data.mp3                # Temporary TTS audio file
│
├── 📁 media/                      # Media Assets Directory
│   ├── 📁 else/                   # General Media Categories
│   │   ├── 📁 me/                 # Personal videos
│   │   │   ├── 🎥 *.mp4
│   │   │   ├── 🎥 *.avi
│   │   │   └── 🎥 *.mkv
│   │   ├── 📁 nolan/              # Christopher Nolan clips
│   │   │   └── 🎥 video files
│   │   ├── 📁 pain/               # Emotional content
│   │   │   └── 🎥 video files
│   │   ├── 📁 song/               # Music videos
│   │   │   └── 🎥 video files
│   │   ├── 📁 world/              # World-related content
│   │   │   └── 🎥 video files
│   │   ├── 🎥 black.mp4           # Black hole video
│   │   └── 🎥 love.mp4            # Love-themed video
│   └── 📁 shivam/                 # User-specific content (Baldev)
│       └── 🎥 video files
│
├── 📁 edge_tts/                   # Edge TTS Module (if separate)
│   ├── 📄 __init__.py
│   ├── 📄 exceptions.py           # Custom exceptions
│   └── 📄 constants.py            # TTS constants
│
└── 📁 dependencies/               # External Dependencies
    └── 🔧 VLC Media Player        # F:\Program Files\VideoLAN\VLC\vlc.exe
└── README.md # Combined documentation

---

## 💬 E3N – AI Voice Assistant

### 🔑 Features

- 🧠 **AI Conversation** – Pi.ai integration for human-like responses
- 🎙️ **Voice Recognition** – Google Speech Recognition
- 🗣️ **Edge TTS** – High-quality, customizable voice synthesis (en-CA-LiamNeural, en-US-AriaNeural, etc.)
- 💡 **Web Automation** – Interacts with web services using Selenium
- 🎛️ **Media Control** – Built-in audio playback via Pygame
- 🖥️ **Cross-platform** – Works on Windows, macOS, and Linux

### ⚙️ Setup

```bash
cd e3n/
pip install -r requirements.txt

Or install manually:

bash
Copy
Edit
pip install pygame speechrecognition selenium edge-tts aiohttp wikipedia certifi psutil


▶️ Run
bash
Copy
Edit
# Basic voice assistant
python ar.py

# Full AI assistant
python aiii.py
