#!/usr/bin/env python3
"""
transcribe.py

Command line tool to convert MP3 audio files to text using the
open-source OpenAI Whisper model running locally.

Example:
    python transcribe.py audio1.mp3 audio2.mp3 --model base
"""

import argparse
import logging
import os
import sys
from typing import List

import whisper


# -----------------------------------------------------
# Logging Configuration
# -----------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


# -----------------------------------------------------
# Utility Functions
# -----------------------------------------------------
def validate_audio_files(files):
    """
    Validate input audio files.

    Checks:
    - File exists
    - File format supported
    """

    SUPPORTED_FORMATS = (".mp3", ".m4a", ".wav", ".flac")

    for file in files:
        if not os.path.exists(file):
            logger.error(f"File does not exist: {file}")
            sys.exit(1)

        if not file.lower().endswith(SUPPORTED_FORMATS):
            logger.error(
                f"Unsupported file format: {file}. Supported formats: {SUPPORTED_FORMATS}"
            )
            sys.exit(1)

            
def load_whisper_model(model_name: str):
    """
    Load Whisper model.

    The model is automatically downloaded the first time
    and cached locally for future runs.
    """
    try:
        logger.info(f"Loading Whisper model: {model_name}")
        model = whisper.load_model(model_name)
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Failed to load Whisper model: {e}")
        sys.exit(1)


def transcribe_audio(model, audio_file: str) -> str:
    """
    Transcribe a single audio file using Whisper.
    """
    try:
        logger.info(f"Transcribing: {audio_file}")
        result = model.transcribe(audio_file)
        return result["text"].strip()
    except Exception as e:
        logger.error(f"Failed to transcribe {audio_file}: {e}")
        return "Transcription failed."


def print_transcription(file: str, text: str) -> None:
    """
    Print formatted transcription output.
    """

    print("\n-------------------------------------")
    print(f"File: {file}")
    print("Transcription:")
    print(text)
    print("-------------------------------------")


# -----------------------------------------------------
# Main Application Logic
# -----------------------------------------------------
def main():
    """
    Main CLI entry point.
    """

    parser = argparse.ArgumentParser(
        description="Convert MP3 audio files to text using OpenAI Whisper locally."
    )

    parser.add_argument(
    "audio_files",
    nargs="+",
    help="Audio files to transcribe (.mp3, .m4a, .wav, .flac)"
    )

    parser.add_argument(
        "--model",
        default="base",
        help="Whisper model to use (tiny, base, small, medium, large). Default: base"
    )

    args = parser.parse_args()

    audio_files = args.audio_files
    model_name = args.model

    # Validate files
    validate_audio_files(audio_files)

    # Load model once
    model = load_whisper_model(model_name)

    # Transcribe files
    for audio in audio_files:
        text = transcribe_audio(model, audio)
        print_transcription(audio, text)


# -----------------------------------------------------
# Script Entry Point
# -----------------------------------------------------
if __name__ == "__main__":
    main()