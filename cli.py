import sys
from multi_value_dict import MultiValueDictionary

HELP_TEXT = """
) This is a command-line application that stores a multi-value dictionary.
) 
) Available Commands:
) -----------------------------------------------------------------------------------------------
) ADD <key> <member>          - Adds a member to the key
) MEMBERS <key>               - Lists all members of the key
) KEYEXISTS <key>             - Checks if the key exists
) MEMBEREXISTS <key> <member> - Checks if a member exists for a key
) ALLMEMBERS                  - Lists all members from all keys
) ITEMS                       - Lists all keys and their members
) KEYS                        - Lists all keys
) 
) REMOVE <key> <member>       - Removes a member from the key
)                               (If the last member is removed from the key, the key is removed)
) REMOVEALL <key>             - Removes all members of the key, and the key is also removed
) CLEAR                       - Clears all keys and members
) 
) RE                          - Clears the dictionary and console screen
) HELP                        - Displays this help message
) QUIT                        - Quits the application
) -----------------------------------------------------------------------------------------------
"""

def main():
    dictionary = MultiValueDictionary()
    print(") Enter 'HELP' to displays help message")

    while True:
        command = input("> ").strip().split(" ", 2)
        action = command[0].upper()

        if action == "KEYS":
            print("\n".join(dictionary.keys()))
        
        elif action == "MEMBERS" and len(command) > 1:
            print("\n".join(dictionary.members(command[1])))

        elif action == "ADD" and len(command) > 2:
            print(dictionary.add(command[1], command[2]))

        elif action == "REMOVE" and len(command) > 2:
            print(dictionary.remove(command[1], command[2]))

        elif action == "REMOVEALL" and len(command) > 1:
            print(dictionary.remove_all(command[1]))

        elif action == "CLEAR":
            print(dictionary.clear())

        elif action == "KEYEXISTS" and len(command) > 1:
            print(dictionary.key_exists(command[1]))

        elif action == "MEMBEREXISTS" and len(command) > 2:
            print(dictionary.member_exists(command[1], command[2]))

        elif action == "ALLMEMBERS":
            print("\n".join(dictionary.all_members()))

        elif action == "ITEMS":
            print("\n".join(dictionary.items()))

        elif action == "QUIT":
            print(") App is closing. Goodbye!")
            sys.exit()

        # Gives some room when user enter nothing
        elif action == "":
            print("")       

        # Clears the dictionary and console screen
        elif action == "RE":
            dictionary.reset()
            print("Enter 'HELP' to displays help message")

        # Displays the help message
        elif action == "HELP":
            print(HELP_TEXT)

        else:
            print(") ERROR, unknown command. Enter 'HELP' to displays help message")

if __name__ == "__main__":
    main()
