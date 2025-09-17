import os
import pyautogui
from core.gemini_engine import ask_gemini
from core.memory import clear_memory

def execute_command(cmd):
    cmd = cmd.lower()
    if "open notepad" in cmd:
        os.system("notepad")
        return "Opening Notepad"
    elif "screenshot" in cmd:
        path = "data/screenshots/screenshot.png"
        pyautogui.screenshot(path)
        return "Screenshot saved."
    elif "open browser" in cmd:
        os.system("start chrome")
        return "Opening browser"
    elif "clear memory" in cmd:
        clear_memory()
        return "Memory cleared."
    else:
        return ask_gemini(cmd)
