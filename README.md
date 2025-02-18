# Multi-Value Dictionary (Python)
│── multi_value_dict.py  # Main application logic

│── cli.py               # Command-line interface

│── README.md            # Instructions

## Description
A command-line application that stores a multi-value dictionary.

## Requirements
- Python 3.xx

## Installation
Navigate to project root and run: 
python cli.py

## Available Commands:
-----------------------------------------------------------------------------------------------
ADD <key> <member>          - Adds a member to the key

MEMBERS <key>               - Lists all members of the key

KEYEXISTS <key>             - Checks if the key exists

MEMBEREXISTS <key> <member> - Checks if a member exists for a key

ALLMEMBERS                  - Lists all members from all keys

ITEMS                       - Lists all keys and their members

KEYS                        - Lists all keys

REMOVE <key> <member>       - Removes a member from the key
                              (If the last member is removed from the key, the key is removed)
                              
REMOVEALL <key>             - Removes all members of the key, and the key is also removed

CLEAR                       - Clears all keys and members

RE                          - Clears the dictionary and console screen

HELP                        - Displays this help message

QUIT                        - Quits the application

-----------------------------------------------------------------------------------------------
