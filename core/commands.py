import os
import pyautogui
import webbrowser
from core.gemini_engine import ask_gemini
from core.memory import clear_memory

def execute_command(cmd):
    cmd = cmd.lower()

    # System commands
    if "open notepad" in cmd: os.system("notepad"); return "Opening Notepad."
    if "open paint" in cmd: os.system("mspaint"); return "Opening Paint."
    if "open calculator" in cmd: os.system("calc"); return "Opening Calculator."
    if "open browser" in cmd or "open chrome" in cmd: webbrowser.open("https://www.google.com"); return "Opening Chrome browser."
    if "open youtube" in cmd: webbrowser.open("https://www.youtube.com"); return "Opening YouTube."
    if "open github" in cmd: webbrowser.open("https://www.github.com"); return "Opening GitHub."
    if "screenshot" in cmd:
        os.makedirs("data/screenshots", exist_ok=True)
        path = "data/screenshots/screenshot.png"
        pyautogui.screenshot(path)
        return f"Screenshot saved to {path}."
    if "shutdown" in cmd: os.system("shutdown /s /t 5"); return "Shutting down PC."
    if "restart" in cmd: os.system("shutdown /r /t 5"); return "Restarting PC."
    if "lock pc" in cmd: os.system("rundll32.exe user32.dll,LockWorkStation"); return "PC locked."
    if "clear memory" in cmd: clear_memory(); return "Jarvis memory cleared."

    # Mouse/keyboard commands
    if "move mouse up" in cmd: pyautogui.moveRel(0, -100); return "Mouse moved up."
    if "move mouse down" in cmd: pyautogui.moveRel(0, 100); return "Mouse moved down."
    if "move mouse left" in cmd: pyautogui.moveRel(-100, 0); return "Mouse moved left."
    if "move mouse right" in cmd: pyautogui.moveRel(100, 0); return "Mouse moved right."
    if "click mouse" in cmd: pyautogui.click(); return "Mouse clicked."
    if "double click" in cmd: pyautogui.doubleClick(); return "Mouse double clicked."
    if "type" in cmd: text = cmd.replace("type", "").strip(); pyautogui.typewrite(text); return f"Typing: {text}"

    # Fallback to Gemini AI
    return ask_gemini(cmd)
