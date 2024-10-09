# AI Voice Assistant

An intelligent voice-controlled assistant built with Python, capable of performing various tasks and engaging in conversations.

## Features

- Voice recognition and text-to-speech capabilities
- Web browsing and search functionality
- System controls (shutdown, restart, lock)
- File and application management
- Music and video playback
- Time and date information
- Basic calculations
- Weather forecasts
- News headlines
- Jokes and fun facts
- Conversational abilities

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-voice-assistant.git
   cd ai-voice-assistant
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up API keys:
   - Obtain API keys for OpenWeatherMap and NewsAPI
   - Add your API keys to the `command.py` file:
     ```python
     OPENWEATHER_API_KEY = "your_openweather_api_key"
     NEWS_API_KEY = "your_newsapi_key"
     ```

## Usage

Run the main script to start the AI assistant:


## ABOUT THE PROJECT 

The assistant will greet you and wait for your voice commands. You can ask it to perform various tasks or engage in conversation.

## Available Commands

Here are some example commands you can use:

- "Search on YouTube for [query]"
- "Open Google and search for [query]"
- "Play music"
- "What's the time?"
- "Set a timer for [duration]"
- "What's the weather forecast for [city]?"
- "Tell me the top headlines"
- "Tell me a joke"
- "What can you do?"

For a full list of available commands, refer to the `execute_command` function in `command.py`.

## Project Structure

- `main.py`: The entry point of the application
- `assistant.py`: Contains the `Assistant` class for speech recognition and synthesis
- `command.py`: Implements the `execute_command` function and various helper functions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) for text-to-speech functionality
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) for speech recognition capabilities
- [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit) for various utilities
- [pyautogui](https://github.com/asweigart/pyautogui) for GUI automation
- [psutil](https://github.com/giampaolo/psutil) for system and process utilities
- [requests](https://github.com/psf/requests) for making HTTP requests
- [wikipedia](https://github.com/goldsmith/Wikipedia) for accessing Wikipedia content
- [newsapi-python](https://github.com/mattlisiv/newsapi-python) for fetching news headlines

## Contact

If you have any questions or feedback, please open an issue on GitHub or contact [ranajayant527@example.com].
