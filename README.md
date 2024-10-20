# voice-assistant
Machine Learning Project - voice assistant/ virtual assistant

```markdown
# Voice Assistant

A versatile, customizable **Voice Assistant** that responds to voice commands to perform various tasks such as reminders, setting alarms, retrieving weather information, and much more. This project is built using Python and integrates both online and offline speech recognition for seamless operation in any environment.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [APIs and Tools](#apis-and-tools)
- [Methodology](#methodology)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

## Features
- **Voice Command Recognition**: The assistant listens for wake words and responds to user commands.
- **Online/Offline Recognition**: Uses Google’s API for online recognition and Vosk for offline recognition when internet access is unavailable.
- **Conversational Features**: Engage in basic conversations and interactive responses.
- **Web-based Queries**: Retrieves online information such as weather, calculations, and factual queries using WolframAlpha.
- **APIs Integration**: Uses multiple APIs for advanced functionalities like web scraping, weather updates, and more.
  
## Installation

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package installer)

### Dependencies

install the following key packages manually:
```bash
pip install speechrecognition pyttsx3 vosk pyaudio requests wolframalpha wikipedia speedtest webbrowser pywhatkit
```

### Vosk Model (for Offline Speech Recognition)
Download the Vosk language model:
1. Visit the [Vosk Model Website](https://alphacephei.com/vosk/models)
2. Extract the downloaded model to your project directory.
3. Update the path to the model in the script.

## Usage

1. **Run the Assistant**:
   To start the voice assistant, simply run the main script:
   ```bash
   python voice_assistant.py
   ```

2. **Commands**:
   - **Wake Phrases**: "Wake up", "Get up", "Hello assistant", "Hey assistant"
   - **Information Queries**: "What's the weather?", "Tell me a joke", "Search google for Python tutorials"
   - **System Commands**: "Open Notepad", "Close all tabs"
   
3. **Offline Mode**:
   The assistant will automatically switch to offline recognition (Vosk) when no internet connection is detected.

## APIs and Tools
- **SpeechRecognition**: For recognizing speech through Google’s API.
- **Vosk**: For offline voice recognition when the internet is unavailable.
- **pyttsx3**: For converting text responses into speech.
- **WolframAlpha API**: For answering factual questions and performing computations.
- **PyAutoGUI**: For controlling basic system operations (like opening/closing applications).
- **Speedtest**: For getting the download and upload speed.
- **Wikipedia**: For getting the information from wikipedia.
  
## Methodology

- **Speech Recognition**: Uses Google’s API for accurate online voice recognition and Vosk for offline speech-to-text conversion.
- **Task Scheduling**: Implements Python’s built-in libraries to handle timers, reminders, and alarms.
- **NLP Processing**: Uses basic parsing to interpret user commands and map them to predefined actions.
- **APIs**: Queries external services like WolframAlpha for knowledge-based queries.
- **Hybrid Mode**: Automatically chooses between online and offline modes based on network availability.

## Future Improvements
- **Customizable Wake Word**: Allow users to configure their own wake word.
- **Extended Support for More Languages**: Add support for additional languages beyond English.
- **Deep Learning for Enhanced NLP**: Implement advanced NLP techniques for more natural interactions.
- **Mobile Integration**: Full-fledged Android/iOS app with local recognition.

## Contributors
- Seetaram Prajapat(https://github.com/Srprajapat) - Developer

---

Feel free to contribute to this project by submitting issues or pull requests. If you have any questions, feel free to contact us.

```

### Notes:
- Replace `"voice_assistant.py"` with the actual name of your main script.
- Update `"yourprofile"` and contributor names as needed.

This **README.md** provides a detailed overview of your project, its features, how to install and use it, and potential areas for improvement, making it GitHub-ready. Let me know if you need any further customization!
