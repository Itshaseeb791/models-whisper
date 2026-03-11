🎙️ Whisper Local Audio Transcriber

A simple, production-style Python command line application that converts audio files into text using the open-source OpenAI Whisper speech recognition model, running completely locally.

This tool allows you to transcribe audio files such as MP3, M4A, WAV, and FLAC directly from the terminal without requiring any external API or internet connection after the model is downloaded.

🚀 Features

🎧 Transcribe audio files to text

🧠 Uses OpenAI Whisper open-source model

💻 Runs 100% locally

📥 Automatic model download on first run

⚡ Supports multiple Whisper models

🧾 Supports multiple audio formats

🛠 Built with clean, modular Python code

📜 Simple command line interface

📊 Clear and formatted terminal output

📁 Supported Audio Formats

The application supports the following audio formats:

.mp3

.m4a

.wav

.flac

🧠 Whisper Models

You can choose different Whisper models depending on speed and accuracy.

Model	Speed	Accuracy
tiny	⚡ Very Fast	Low
base	Fast	Good
small	Medium	Better
medium	Slow	High
large	Very Slow	Best

Default model:

base
📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/whisper-transcriber.git
cd whisper-transcriber
2️⃣ Install Python Dependencies

Make sure you have Python 3.9+ installed.

pip install -r requirements.txt
3️⃣ Install FFmpeg

Whisper requires FFmpeg to process audio files.

Windows

Download from:

https://www.gyan.dev/ffmpeg/builds/

Extract and add the bin folder to your System PATH.

Verify installation:

ffmpeg -version
▶️ Usage

Basic command:

python transcribe.py audio_file.m4a

Transcribe multiple files:

python transcribe.py audio1.mp3 audio2.m4a

Select a specific Whisper model:

python transcribe.py audio1.mp3 audio2.mp3 --model small
💻 Example Output
INFO: Loading Whisper model: base
INFO: Model loaded successfully.
INFO: Transcribing: test.m4a

-------------------------------------
File: test.m4a
Transcription:
Hello everyone, welcome to this Whisper transcription demo.
-------------------------------------
⚙️ How It Works

The program loads a Whisper speech recognition model.

If the model is not present locally, it is automatically downloaded.

The audio file is processed using FFmpeg.

Whisper converts speech into text.

The transcription is printed to the terminal.

After the first run, the model is cached locally and no internet connection is required.

📂 Project Structure
whisper-transcriber
│
├── transcribe.py
├── requirements.txt
└── README.md
📚 Requirements

Python 3.9+

FFmpeg

PyTorch

OpenAI Whisper

Dependencies are listed in:

requirements.txt
🧪 Example Test

Run a quick test:

python transcribe.py sample_audio.m4a --model tiny
🔒 Privacy

This tool runs entirely on your local machine.
No audio is uploaded to external servers, ensuring full privacy and security.

📜 License

This project is open-source and available under the MIT License.

🙌 Acknowledgements

OpenAI Whisper

PyTorch

FFmpeg

⭐ If you find this project useful, consider starring the repository on GitHub!