from mpmath import mp
from os.path import exists
import json
import re
from pynput import keyboard
from pyfiglet import figlet_format 

from errors import MissingPropertyError, MissingFileError, Tab

import os
import sys
sys.tracebacklimit=0
sys.dont_write_bytecode = 1


class PITrainer:
    def __init__(self):
        self.counter = 1

    def on_release(self, key):
        if key == keyboard.Key.enter:
            os.system("cls" if os.name == "nt" else "clear")
            print(figlet_format(pi[0], font = "univers"))
            if screen_counter: print(f"{self.counter+1}/{digits}") 
            pi.pop(0)
            self.counter += 1
        if key == keyboard.Key.tab:
                raise Tab  # just used to trigger the exception at the listener.join()
        else:
            return

    def main(self):
        
        if not exists("config.json"):

            default = { "digits": "0" }

            f = open("config.json", "x")
            f.write(json.dumps(default, indent=4))

            raise MissingFileError("Config file is missing!")
        else:
            global cfg
            cfg = json.loads(open("config.json", "r").read())
            global digits
            digits = str(cfg.get("digits"))
            global screen_counter
            screen_counter = cfg.get("screen_counter")
        
        if screen_counter is None:
            raise MissingPropertyError("Config file is missing the `screen_counter` property!")
        if screen_counter is not None and not isinstance(screen_counter, bool):
            raise TypeError("`screen_counter` property must be a boolean!")
        if digits is None:
            raise MissingPropertyError("Config file is missing the `digits` property!")
        if digits is not None and not bool(re.compile("^[0-9]+$").search(digits)):
            raise TypeError("`digits` property must be an integer!")
        
        mp.dps = int(digits) + 1

        global pi
        pi = list(str(mp.pi)[4:])
        pi.insert(0, "3.14") # 3.14 is wrapped in one element since everyone knows it

        print("Press Enter to start!")
        while len(pi) != 0:
            with keyboard.Listener(on_release=self.on_release) as listener:
                try:
                    listener.join()
                except Tab: # somehow the exception is only called when there's an IndexError
                    if pi[0] == "3.14":
                        open("score.txt", "w").write("0")
                    else:
                        open("score.txt", "w").write(str(self.counter))
                except:
                    if any(int(digits) == x for x in [0, 1, 2]) and len(pi) == 0:
                        open("score.txt", "w").write("2")
                    else:
                        open("score.txt", "w").write(digits)
                finally:
                    os.system("cls" if os.name == "nt" else "clear")
                    exit(0)




if __name__ == "__main__":
    pi_trainer = PITrainer()
    pi_trainer.main()