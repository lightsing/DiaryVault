import re
from getpass import getpass

def get(prompt="Please enter a password:"):
    print("---------Security  Instructions---------")
    print("Password should follow the standards:\n\
At least 8 characters\n\
Must be restricted to have:\n\
  uppercase letters: A-Z\n\
  lowercase letters: a-z\n\
  numbers: 0-9\n\
  any of the special characters: @#$%^&+=")
    while True:
        password = getpass(prompt)
        if re.search(r'[A-Z]',password) and \
           re.search(r'[a-z]',password) and \
           re.search(r'[0-9]',password) and \
           re.search(r'[@#$%^&+=]',password) and \
           ' ' not in password and \
           len(password) > 7:
            break
        else:
            print("Password isn't strong enough. Please choose a different one.")
    return password
