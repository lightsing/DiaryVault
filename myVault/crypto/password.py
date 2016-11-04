from getpass import getpass


def get(prompt="Please enter a password:"):
    print("\nPassword should be at least 12 characters.")
    while True:
        password = getpass(prompt)
        if len(password) > 7:
            break
        else:
            print("Password isn't strong enough. Please choose a different one.")
    return password
