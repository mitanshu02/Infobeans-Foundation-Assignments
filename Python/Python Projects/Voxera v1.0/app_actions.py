import webbrowser
import subprocess
import pyautogui
import time
from urllib.parse import quote
from config import WEBSITES, APPLICATIONS

def open_website(name):
    url = WEBSITES.get(name)
    if url:
        webbrowser.open(url)
        return True

    return False

def open_application(name):
    app = APPLICATIONS.get(name)
    if not app:
        return False
    subprocess.Popen(["cmd", "/c", "start", "", app],shell=False)
    return True

def open_installed_app(name):
    pyautogui.hotkey("win", "s")
    time.sleep(1)
    pyautogui.write(name, interval=0.05)
    time.sleep(2)
    pyautogui.press("enter")
    return True

def search_web(query):
    query = quote(query)
    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)
    return True