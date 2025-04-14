import argparse
import os

def display_help():
    print('''
|   -h or --help   ==> help you command to run                       |
|    anasc2       ==> run attack browser javascript                 |
|    code          ==> run tool check website found or not found     |
|    path          ==> scan path link attack                         |
''')

def anasc2():
    print("-"*40)
    print("#             anas              #")
    print("-"*40)
    try:
        os.system("python3 app.py")
    except Exception as e:
        print(f"Error running app.py: {e}")

def code():
    try:
        os.system("python3 status_code.py")
    except Exception as e:
        print(f"Error running status_code.py: {e}")

def search():
    try:
        os.system("python3 massar.py")
    except Exception as e:
        print(f"Error running massar.py: {e}")

parser = argparse.ArgumentParser(description="Multi-tasking Web Application Penetration Testing Tool!")
parser.add_argument("command", choices=['search', 'anasc2', 'help', 'code'], help="commands to Run")
args = parser.parse_args()

if args.command == 'help':
    display_help()

if args.command == 'anasc2':
    anasc2()

if args.command == 'code':
    code()

if args.command == 'search':
    search()

