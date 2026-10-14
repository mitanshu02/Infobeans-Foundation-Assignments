import os
import pyautogui
from datetime import datetime


def take_screenshot():
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    now = datetime.now()
    name = now.strftime("screenshot_%Y%m%d_%H%M%S.png")
    path = os.path.join(folder, name)
    image = pyautogui.screenshot()
    image.save(path)

    return path

if __name__ == "__main__":
    result = take_screenshot()
    print(f"Screenshot saved at: {result}")