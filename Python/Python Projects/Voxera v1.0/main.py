from voice_input import listen
from voice_output import speak
from command_processor import process_command

def main():
    speak("Voxera is ready. How can I help you?")

    while True:
        command = listen()
        if not command:
            continue

        command = command.lower().strip()
        if command in ("exit", "quit", "stop"):
            speak("Goodbye.")
            break
        
        result = process_command(command)

        if isinstance(result, str):
            speak(result)
        elif result:
            speak("Action completed.")
        else:
            speak("Sorry, I don't understand that command.")


if __name__ == "__main__":
    main()