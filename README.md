# 🤖 Ethan – AI Robot for NAAC Accreditation

**Ethan** is a semi-interactive AI robot built using e-waste, combining speech-based interaction, IoT-driven motion, and custom-designed 3D body parts. Developed for the **NAAC accreditation visit (Dec 4, 2023)**, Ethan showcases the integration of AI, electronics, and sustainable design to demonstrate institutional innovation.

---

## 🔧 Features

- 🎤 **AI Module**  
  - Real-time **speech recognition** using Python libraries  
  - **Text-to-speech (TTS)** synthesis for natural voice output  
  - Enables bidirectional human–robot conversation  

- 📐 **3D Design**  
  - Body and structure modeled using **Pepakura** and **AutoCAD**  
  - Fabricated using cardboard and upcycled electronic waste  
  - Compact and static design optimized for indoor display

- 🌐 **IoT System**  
  - Built with **Arduino Uno**  
  - **Ultrasonic proximity sensors** detect nearby presence  
  - Triggers **servo-controlled head movements** for interaction  

---

## 💡 Inspiration

The project was developed as a technical demonstration during the NAAC peer team’s institutional visit. Ethan represents:
- Smart integration of **AI + IoT**
- Eco-conscious design using **recycled materials**
- Student-led innovation from the **Electronics and Communication Engineering** department

---

## 🛠️ Tech Stack

| Component | Tools / Libraries |
|----------|--------------------|
| AI Voice | Python, `speech_recognition`, `pyttsx3`, `gTTS` |
| Hardware | Arduino Uno, Ultrasonic Sensor (HC-SR04), Servo Motor |
| Design   | AutoCAD, Pepakura Designer |
| Deployment | Standalone system (no internet dependency) |

---

## 📸 Demo

<img src="demo/ethan_photo.jpg" width="300"/>  
*Ethan on display during the NAAC visit (Dec 4, 2023)*

> 💬 *"Hello! I am Ethan. Welcome to our department!"*

(You can add a video here: upload to GitHub or link a YouTube demo)

---

## 🔌 Getting Started

### Prerequisites
- Python 3.8+
- Arduino IDE
- Pepakura Viewer (optional, for 3D model editing)

### 1. Clone the Repository
```bash
git clone https://github.com/ShivamKum4r/Ethan.git
cd Ethan
