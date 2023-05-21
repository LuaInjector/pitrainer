import sys
sys.dont_write_bytecode = 1

class MissingPropertyError(Exception):
    def __init__(self, message):
        self.message = message

class MissingFileError(Exception):
    def __init__(self, message):
        self.message = message

##########################################

class Tab(Exception):
    def __init__(self):
        self.message = "_"

__all__ = [
    "MissingPropertyError",
    "MissingFileError",

    "Tab"
]