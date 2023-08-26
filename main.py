# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Initial Release Date: 05/08/2023

import pyautogui
import time
import msvcrt as m
import os
import sys
import json
from screeninfo import get_monitors
from version import version


def main():
    try:
        print_intro()   
        png_path, confidence = load_settings() 
        do_loop(png_path, confidence)
    except Exception as e: error_out(e)
    return

def print_intro():
    print(f"""
######################################################
######################################################
####                                              ####
####    Baldurs Gate 3 Auto Join Conversations    ####
####                                              ####
######################################################
######################################################

Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
Release Date: 05/08/2023
Version: v{version}
        """)
    return

def load_settings():
    print("loading settings from settings.json")
    with open("settings.json", "r") as f:
        settings = json.load(f)
        confidence = float(settings["confidence"])
        print(f"setting confidence to {confidence}")
        resolution_height = settings["resolution_height"]
        if resolution_height == "auto-detect":
            print("auto detecting screen height")
            for m in get_monitors():
                if m.is_primary:
                    resolution_height = m.height
                    print(f"detected screen height {resolution_height}")
        png_path = f"listen-in-{resolution_height}.png"
        print(f"using png path {png_path}")
    return png_path, confidence

def do_loop(png_path, confidence):
    print("-------------------------------------")
    print("Trying to locate the listen in button")
    while True:
        try:
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen(png_path, confidence=confidence)
            print(f"Clicking on listen in button on ({x}, {y})")
            pyautogui.click(x, y)
        except TypeError as e: pass
    return

def error_out(e):
    print(e)
    print("Press any key to exit...", end="", flush=True)
    m.getch()
    exit(0)
    return

if __name__ == "__main__":
    main()
