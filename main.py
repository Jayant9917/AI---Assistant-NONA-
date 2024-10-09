from assistant import Assistant
from command import execute_command

if __name__ == "__main__":
    assistant = Assistant()
    assistant.wishMe()
    while True:
        query = assistant.takeCommand().lower()
        execute_command(query, assistant)

