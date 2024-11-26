"""This is an attempt at creating a simple password generator"""

import random
from colorama import Fore, Style, init
import string

def main():
    """
    Here is the main function.
    Hopefully this works
    """

    # begin the loop
    while True: 

        # Get params from user and reset the style if there is any applied
        strength = input(Style.RESET_ALL + "Choose the password strength you wish to use.\n Options are: weak, middling, strong, beast, and finished.\n\n").strip().lower()
       # Break the loop if the user inputs finished.
        if strength == "finished":
            break

        length = input("\n\nChoose a password length.\n It is suggested to have at least a 12 character password and to store it in a vault.\n\n")
        
        # Break the loop if the user inputs done.
        if length == "finished":
            break
        
        # Confirm what the use inputted
        print('\n\nYou have chosen a ' + strength + ' password with ' + length + ' characters.\n If you are finished, type "Done"\n\n')
            
        # Create charset lists that enable increasing in complexity
        str_options = {
            "weak": list(string.ascii_lowercase),
            "middling": list(string.ascii_lowercase + string.ascii_uppercase),
            "strong": list(string.ascii_lowercase + string.ascii_uppercase + string.digits),
            "beast": list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) 
        }
        length = int(length)
        
        # Flow control to the type of password to be created   
        if strength in str_options:
            password_gen(str_options[strength], length)
        else:
            print("Please choose from weak, middling, strong, beast, or done ")


def password_gen(chars, char_num):
    '''
    This will create a password with the specified charset
    '''
    password = random.choices(chars, k=char_num)
    print("Here is your  password: " + Fore.RED + "".join(password) + Style.RESET_ALL)

main()
