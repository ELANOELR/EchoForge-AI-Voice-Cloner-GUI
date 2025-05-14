
# EchoForge – Offline AI Voice Cloner

## Overview

EchoForge is an offline GUI interface for voice cloning and local text-to-speech synthesis.
It is designed for content creators, meme editors, voiceover artists, and AI enthusiasts.

## Folder Structure

```
echo_gui.py             → Main GUI launcher  
audio_engine.py         → Decrypts and runs core engine  
core_audio_engine.dat   → Encrypted native module (.exe)  
requirements.txt        → Python dependencies  
gui_preview.png         → Screenshot of the interface  
README.md               → Project description  
LICENSE                 → MIT license  
.gitignore              → Git exclusions  
init_and_push.sh        → GitHub upload script  
```

## Installation

1. Make sure you have Python 3.10 or higher installed.
2. Open terminal or command prompt in this directory.
3. Run the following commands:

```bash
pip install -r requirements.txt
python echo_gui.py
```

## Notes

- All processing runs locally.
- No internet or login required.
- Intended for educational and demonstration purposes only.
