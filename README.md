# AnasC2 🕷️

![AnasC2 Logo](AC2.png)

**AnasC2** is a comprehensive browser-based Command & Control (C2) tool designed for cybersecurity testing and Red Team operations. Developed in Python with Flask and Socket.IO, this tool offers a variety of modules for managing target devices, scanning websites, and testing HTTP status codes.  
Developed with passion by [anasslabrini](https://github.com/anasslabrini).  
MyWebSite: [anaslabrini](https://anaslabrini.netlify.app)

---

## 📦 Features Overview

- **Browser C2 Interface:** 
  - Real-time control over target browsers using WebSocket communication.
  - Ability to redirect clients and display custom alert messages.
- **HTTP Status Code Checker:**
  - Test and verify the HTTP response status of multiple URLs.
- **Directory Scanner:**
  - Scan target websites for common directories using a custom wordlist.
- **Centralized Launcher:**
  - Manage and execute various modules through a single launcher script.
  
---

## 🧰 Requirements

Before using this tool, please ensure that you have Python 3 and `pip` installed.

### 📥 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Installation

1. Clone this repository:

```bash
git clone https://github.com/anasslabrini/AnasC2.git
cd AnasC2
```
2. Run the Main Server (Browser C2):
This starts the Flask server that provides both the victim and admin interfaces.


```bash
python3 app.py
```
Victim Page: Accessible at: http://127.0.0.1:5000/

Admin Panel: Accessible at: http://127.0.0.1:5000/admin
3. Launch Additional Modules via the Central Launcher:

```bash
python3 boss.py help
```
The boss.py script acts as the controller to manage all other modules.

Display Help Menu:


```bash
python3 boss.py help
```
Run the Browser C2 Attack Module:

```bash
python3 boss.py anasc2
```
HTTP Status Code Checker (status_code.py):


```bash
python3 boss.py code
```
Directory Scanner (massar.py):

```bash
python3 boss.py search
```

---

## 📁 File Structure

```
AnasC2/
├── app.py               # Main Flask application and Socket.IO server.
│                        # Sets up endpoints for the victim page (/)
│                        # and admin panel (/admin) and handles WebSocket events.
│
├── boss.py              # Central launcher script that controls all modules.
│                        # Provides command-line interface with options:
│                        #    - help: Displays usage instructions.
│                        #    - anasc2: Runs the main browser attack module.
│                        #    - code: Launches HTTP status checking (status_code.py).
│                        #    - search: Executes directory scanning (massar.py).
│
├── common.txt           # Wordlist file containing common directory names.
│                        # Used by the massar.py script for path scanning.
│
├── massar.py            # Directory/path scanning module.
│                        # Reads URLs from the user and appends paths from common.txt.
│                        # Attempts to access these URLs and reports their HTTP status.
│
├── requirements.txt     # List of Python dependencies required by the project.
│                        # (e.g., Flask, Flask-SocketIO, requests, rich).
│
├── static/
│   └── hook.js          # JavaScript file that runs on the victim's browser.
│                        # Listens for commands (redirect or alert) via Socket.IO
│                        # and executes them (e.g., navigating to a new URL or displaying an alert).
│
├── status_code.py       # Module to check the HTTP status codes for a set of URLs.
│                        # Uses the requests module to fetch URLs and displays their status.
│
└── templates/           # Contains HTML templates and assets for the web interfaces.
    ├── admin.html       # Admin panel interface where operators can send commands (redirect/alert).
    ├── index.html       # Victim page that gets loaded on target machines.
    ├── admin.css        # CSS file for styling the admin panel.
    ├── styles.css       # Additional styling for the web interfaces.
    └── (Images and other assets used by the pages)
```

---

Detailed Explanation of Each Component:

    app.py:

       * Initializes the Flask app and Socket.IO server.

       * Defines routes for the victim page (/) and admin panel (/admin).

       * Handles WebSocket messages to perform actions like URL redirection and displaying alerts.

       * Manages client connections and broadcasts messages to connected clients.

    boss.py:

       * Acts as the main CLI launcher for the tool.

       * Uses Python’s argparse module to parse commands.

       * Provides a simple interface to choose which module to run:

           - anasc2 launches the Flask server.

           - code executes the HTTP status code checker.

           - search runs the directory scanner.

       * Contains a help section that outlines available commands.

    common.txt:

       * Contains a list of common directory names and paths.

       * Utilized by the massar.py module to identify potential hidden directories on a target website.

    massar.py:

       * Prompts the user for a target URL.

       * Iterates through paths listed in common.txt, appending each to the base URL.

       * Makes HTTP requests to each constructed URL and reports if the path is found (status code 200) or not.

    status_code.py:

       * Prompts the user to input multiple URLs.

       * Checks each URL for its HTTP status code using the requests library.

       * Provides a detailed status update using rich formatted output for better readability.

    static/hook.js:

       * Runs in the client’s browser.

       * Establishes a connection to the server via Socket.IO.

       * Listens for commands from the admin panel and, based on the command:

           - Redirects the browser to a specified URL.

           - Displays an alert message.

    templates Directory:

       * Contains all HTML templates:

           - index.html serves as the victim page.

           - admin.html is the control panel where commands (like redirect or alert) are issued.

       * Includes associated style files (CSS) and image assets to present a professional UI

---

## ⚠️ Disclaimer

This tool is intended for educational and authorized testing purposes only.  
The author is not responsible for any misuse or illegal activities.  
Always get written permission before testing systems that aren’t yours.

---

## 🪪 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👨💻 Author

**Anas Labrini**  
📍 Salé, Morocco  
📧 hackthebox.time@gmail.com
Instagram: [anasans005]([https://anaslabrini.netlify.app](https://www.instagram.com/anasans005?igsh=dzNsOXN3Nm9INmVk))
