from config import APPLICATIONS, WEBSITES
from app_actions import open_application, open_website
from help_commands import show_commands, get_commands_text
from screenshot_actions import take_screenshot

def process_command(command):
    command = command.lower().strip()

    if command == "help":
        show_commands()
        return get_commands_text()

    if command == "take screenshot":
        path = take_screenshot()
        print(f"Screenshot saved at: {path}")
        return f"Screenshot saved at: {path}"

    if command.startswith("open "):
        target = command[5:]

        if target in WEBSITES:
            return open_website(target)

        if target in APPLICATIONS:
            return open_application(target)

        return False

    return False