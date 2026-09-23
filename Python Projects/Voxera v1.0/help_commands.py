COMMANDS = {
    "help": "Show the list of available commands",
    "open youtube": "Open YouTube",
    "open google": "Open Google",
    "open github": "Open GitHub",
    "open chatgpt": "Open ChatGPT",
    "open notepad": "Open Notepad",
    "open calculator": "Open Calculator",
    "take screenshot": "Take a screenshot",
    "exit": "Close Voxera"
}


def show_commands():
    print("\nAvailable Commands:\n")

    for command, description in COMMANDS.items():
        print(f"{command:<20} - {description}")

def get_commands_text():
    text = "Available commands are: "

    for command in COMMANDS:
        text += command + ", "

    return text