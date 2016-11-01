import re
from getpass import getpass

def get(prompt="Please enter a password:"):
    print("---------Security  Instructions---------")
    print("Password should follow the standards:\n\
           At least 8 characters\n\
           Must be restricted to:\n  \
               uppercase letters: A-Z\n  \
               lowercase letters: a-z\n  \
               numbers: 0-9\n  \
               any of the special characters: @#$%^&+=")
    while True:
        password = getpass(prompt)
        if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}',password):
            break
        else:
            print("Password not strong enough. Please choose a different one.")
    return password

print(get())
