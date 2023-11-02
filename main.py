import os
import time
import pyfiglet
import sys
import subprocess


def run_PE():
    file = input("Please provide the file path and filename. : ")
    return file

def exit():
    os.system('exit')


def start():
    # Define your text
    text = "Static Malware Scanner"
    subtext = "Welcome to Malware Scanner"

    # Generate ASCII art
    ascii_art = pyfiglet.figlet_format(text)

    # Print the ASCII art with different styles
    print(ascii_art)

    # Adding a line gap
    print("\n")

    # Increase the font size for the subtext
    print("\033[1m\033[37m" + subtext + "\033[0m")  # Large and white color

    # Adding a line gap
    print("\n")

    print("\033[4m" + "PE Header scanner" + "\033[0m")  # Underline

    print("\n")
    
    
    file = run_PE()
    res = subprocess.run(['python3', 'PE_main.py', file])
    return file, res
   
file, res = start()

if res.returncode == 1:
    subprocess.run(['python3', 'quarantine_or_remove.py', file])
