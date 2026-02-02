# Python Voice Assistant

A simple Python-based voice assistant with speech recognition and text-to-speech using speech_recognition and gTTS.

## 📖 Overview

Python Voice Assistant listens to voice commands, recognizes text, processes basic queries, and responds with synthesized speech.

## 🎬 Demo

Run `python voice_assistant.py`, say "time", hear response.

## ✨ Features

### 🎤 STT & TTS
- speech_recognition for listening.
- gTTS for speaking.

### 🛠️ Commands
- "time": Current time
- "hello": Greeting

## 📦 Installation

# Clone
git clone https://github.com/mkyla/python-voice-assistant.git
cd python-voice-assistant

# Install
pip install -r requirements.txt

## 📋 Usage Guide

python voice_assistant.py

Speak commands.

## ⚙️ Configuration

- Uses default microphone.

## 🛠️ Development

### 📁 Project Structure

```
python-voice-assistant/
├── voice_assistant.py    # Main script
├── test_voice_assistant.py # Tests
├── requirements.txt      # Dependencies
├── .github/
│   └── workflows/
│       └── ci.yml        # CI/CD
├── LICENSE               # MIT
└── README.md             # Docs
```

### 🧩 Core Components

1. **voice_assistant.py**: Main loop, recognition, TTS.

### 🛠️ Tech Stack

- Python 3
- STT: speech_recognition
- TTS: gTTS

## 📄 License

MIT