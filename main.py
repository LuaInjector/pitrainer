from mpmath import mp
from os.path import exists
import json
import re
from pynput import keyboard
from pyfiglet import figlet_format 

from errors import MissingPropertyError, MissingFileError

import os
import sys
sys.tracebacklimit=0
sys.dont_write_bytecode = 1

def on_release(key):
    if key == keyboard.Key.enter:
        os.system("cls" if os.name == "nt" else "clear")
        print(figlet_format(pi[0], font = "univers"))
        pi.pop(0)
    if key == keyboard.Key.esc:
            exit(0)
    else:
        return

def main():
    
    if not exists("config.json"):

        default = { "digits": "1000" }

        f = open("config.json", "x")
        f.write(json.dumps(default, indent=4))

        raise MissingFileError("Config file is missing!")
    else:
        global cfg
        cfg = json.loads(open("config.json", "r").read())
        global digits
        digits = str(cfg.get("digits"))
    if digits is None:
        raise MissingPropertyError("Config file is missing the `digits` property!")
    elif not bool(re.compile("^[0-9]+$").search(digits)):
        raise TypeError("`digits` property must be an integer!")
    
    mp.dps = digits

    global pi
    pi = list(str(mp.pi)[4:])
    pi.insert(0, "3.14") # 3.14 is wrapped in one element since everyone knows it

    print("Press Enter to start!")
    while len(pi) != 0:
        with keyboard.Listener(on_release=on_release) as listener:
            try:
                listener.join()
            except: # somehow the exception is only called when there's an IndexError
                os.system("cls" if os.name == "nt" else "clear")
                open("score.txt", "w").write(digits)




if __name__ == "__main__":
    main()