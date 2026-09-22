import webbrowser
import subprocess
from config import WEBSITES,APPLICATIONS

def open_website(name):
    url = WEBSITES.get(name)

    if url:
        webbrowser.open(url)
        return True
    
    return False

def open_application(name):
    app = APPLICATIONS.get(name)

    if app:
        subprocess.Popen([app])
        return True
    return False

