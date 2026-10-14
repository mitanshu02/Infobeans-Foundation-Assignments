import pyautogui

def show_desktop():
    pyautogui.hotkey("win", "d")
    return True

def switch_window():
    pyautogui.hotkey("alt", "tab")
    return True

def open_settings():
    pyautogui.hotkey("win", "i")
    return True

def increase_volume():
    pyautogui.press("volumeup")
    return True

def decrease_volume():
    pyautogui.press("volumedown")
    return True

def toggle_mute():
    pyautogui.press("volumemute")
    return True

def increase_brightness():
    pyautogui.press("brightnessup")
    return True

def decrease_brightness():
    pyautogui.press("brightnessdown")
    return True

def open_file_explorer():
    pyautogui.hotkey("win", "e")
    return True

def close_tab():
    pyautogui.hotkey("ctrl", "w")
    return True

def close_application():
    pyautogui.hotkey("alt", "f4")
    return True