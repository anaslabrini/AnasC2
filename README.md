#AnasC2 Project

## Introduction
AnasC2 is a hacking and automation tool project that aims to facilitate website security inspection and assessment. The project features the ability to execute attacks on websites using JavaScript, verify the status of websites using HTTP status codes, and examine hidden paths (directories) on websites.

## Project Components
The project consists of several scripts and tools:

1. **boss.py**: This is the main script that controls the execution of other scripts such as `status_code.py` and `massar.py`. When run, it can execute various commands.

2. **status_code.py**: A tool for checking the HTTP status of websites entered by the user. The status displays either "site found" or "site not found" based on the status code (e.g., 200, 404).

3. **massar.py**: A tool for examining various paths on a website using a common word list (`common.txt`). The tool searches through possible paths and displays the status of each one.

## Requirements
Before you start using the tool, make sure you have installed the following requirements:
- Python 3
- The `requests` library for interacting with websites
- The `rich` library for improving the user interface

You can install the necessary libraries via the command:
```bash
pip install requests rich
```

## How to Use

### Running the Main Script (`boss.py`)
You can run the main script (`boss.py`) using the following command:
```bash
python3 boss.py <command>
```

### Available Commands:

1. **help**: Display instructions for use
2. **anasc2**: Run a JavaScript browser attack
3. **code**: Check the HTTP status of the site
4. **search**: Scan paths using `massar.py`

### Usage Example:
To run the tool:
```bash
python3 boss.py anasc2
```

To run a status check HTTP:
```bash
python3 boss.py code
```

To scan paths:
```bash
python3 boss.py search
```

## Customization and Editing
- You can modify the list of paths (`common.txt`) to customize the scan according to your needs.
- To extend the tool, you can add more scripts to the main script (`boss.py`) so that they can be run in the same way.

## Notes:
- Ensure that you use the tool legally and with appropriate permissions.
- The tool is intended for security testing purposes only on sites where you have permission to test it.

## Development and Contribution
If you would like to contribute to the development of the tool, you can submit a Pull Request on GitHub. We welcome all contributions!

---

**This project was developed by Anas Labrini.**
