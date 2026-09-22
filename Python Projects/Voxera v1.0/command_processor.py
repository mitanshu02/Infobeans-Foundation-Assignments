from config import APPLICATIONS, WEBSITES
from app_actions import open_application, open_website


def process_command(command):
    command = command.lower().strip()

    if command.startswith("open "):
        target = command[5:]

        if target in WEBSITES:
            return open_website(target)

        if target in APPLICATIONS:
            return open_application(target)

        return False

    return False