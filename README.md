# PI Trainer

Basically a PI Trainer but for mad scientists

# Index

- [Index](#index)
- [Requirements](#requirements)
- [Run](#run)
- [Usage](#usage)
    - [Config](#config)
    - [Keybinds](#keybinds) 


## Requirements

- [Python](https://www.python.org/downloads/) 3.8 or above

## Run

    pip install -r requirements.txt
    py main.py

## Usage

### Config

- `digits` | int or str : it represents the number of digits you want practice/learn<br>
Numbers from `0` to `2` will always give you only `3.14` since it is wrapped in one element and it starts counting the digits after the comma 
- `screen_counter` | boolean: shows the number of digits in the format `counter/digits`
<br><br>

### Keybinds

Enter - Proceeds to the next digit<br>
Tab -  Exits the program
