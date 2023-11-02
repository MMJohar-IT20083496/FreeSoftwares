import os
import shutil
import sys

choice = input("File is detected as malicious. Do you want to quarantine or remove it? (q/r): ")
if choice == "q":
    # Create a quarantine directory if it doesn't exist
    quarantine_dir = "quarantine"
    os.makedirs(quarantine_dir, exist_ok=True)
    # Move the malicious file to the quarantine directory
    try:
        shutil.move(sys.argv[1], os.path.join(quarantine_dir, os.path.basename(sys.argv[1])))
        print("File has been quarantined.")
    except FileNotFoundError:
        print("File not found. No action taken.")
elif choice == "r":
    try:
        os.remove(sys.argv[1])
        print("File has been removed.")
    except FileNotFoundError:
        print("File not found. No action taken.")