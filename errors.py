import sys
sys.dont_write_bytecode = 1

class MissingPropertyError(Exception):
    def __init__(self, message):
        self.message = message

class MissingFileError(Exception):
    def __init__(self, message):
        self.message = message

__all__ = [
    "MissingPropertyError",
    "MissingFileError"
]