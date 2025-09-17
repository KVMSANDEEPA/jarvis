# Jarvis Project

Welcome to the Jarvis Project! This README provides an overview of the project and instructions to set it up.

## Project Description

Jarvis is a personal assistant web application. It is designed to help users manage tasks, set reminders, and organize their daily activities efficiently.

## Python Backend Setup

Follow these steps to set up the Python backend for the Jarvis Project:

1. **Install Python (if not installed)**:
    - Download Python 3.11+ from [python.org](https://www.python.org/).
    - During installation, check "Add Python to PATH".
    - Verify installation:
      ```bash
      python --version
      pip --version
      ```

2. **Install pip packages**:
    - Open Command Prompt or PowerShell.
    - Navigate to your project folder:
      ```bash
      cd C:\xampp\htdocs\jarvis-assistant
      ```
    - Install all dependencies from `requirements.txt`:
      ```bash
      pip install -r requirements.txt
      ```
      This will install:
      - Flask → Web server
      - pyttsx3 → Text-to-speech
      - SpeechRecognition → Voice input
      - pyaudio → Microphone support
      - pyautogui → PC automation (e.g., screenshots, open apps)
      - google-generativeai → Gemini AI

    - **Important**: If `pyaudio` fails to install on Windows, install the wheel manually:
      1. Go to [this site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
      2. Download the matching `.whl` for your Python version.
      3. Install via:
         ```bash
         pip install C:\path\to\PyAudio‑0.2.14‑cp311‑cp311‑win_amd64.whl
         ```

3. **Set Gemini API Key**:
    - Open `config.py` and replace:
      ```python
      GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
      ```
    - Sign up for Gemini AI and get a free API key: [Gemini AI](https://developers.google.com/).

4. **Create folders (if not present)**:
    - Ensure the following folders exist:
      ```bash
      mkdir data
      mkdir data/screenshots
      ```
    - SQLite database (`jarvis.db`) will be created automatically.

5. **Run the project**:
    - Run your Flask server:
      ```bash
      python main.py
      ```
    - You should see something like:
      ```
      * Running on http://127.0.0.1:5000/
      ```

6. **Access the Application**:
    - Open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

7. **Test Functionality**:
    - Type a command in the input box.
    - Press "Send" or "Enter".
    - Click 🎤 to speak commands.
    - Use shortcut buttons like "Open Notepad" or "Screenshot".

---
Happy coding!

## Prerequisites

Before setting up the project, ensure you have the following installed:
- [Software/Tools required, e.g., PHP, Composer, MySQL, etc.]
- XAMPP (for local server setup)

## Setup Instructions

Follow these steps to set up the project:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/jarvis.git
    cd jarvis
    ```

2. **Start XAMPP**:
    - Open XAMPP Control Panel.
    - Start the Apache and MySQL services.

3. **Configure the Database**:
    - Open `phpMyAdmin` at `http://localhost/phpmyadmin`.
    - Create a new database (e.g., `jarvis_db`).
    - Import the SQL file located at `database/jarvis_db.sql`.

4. **Install Dependencies**:
    ```bash
    composer install
    ```

5. **Set Environment Variables**:
    - Copy `.env.example` to `.env`:
      ```bash
      cp .env.example .env
      ```
    - Update `.env` with your database credentials.

6. **Run the Application**:
    - Place the project folder in the `htdocs` directory.
    - Access the application at `http://localhost/jarvis`.

## Useful Commands

- Start XAMPP services:
  ```bash
  xampp-control
  ```
- Run Composer install:
  ```bash
  composer install
  ```
- Access the application:
  Open your browser and navigate to `http://localhost/jarvis`.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the [Your License].

---
Happy coding!