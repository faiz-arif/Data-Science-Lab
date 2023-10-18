import re

def is_valid_password(password):
    # Check if the password length is at least 6 characters
    if len(password) < 6:
        print("password should contain atleast 6 characcters")
        return False
    

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        print("password should contain atleast one lowercase")
        return False

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        print("password should contain atleast one uppercase")
        return False

    # Check if the password contains at least one digit
    if not re.search(r'[0-9]', password):
        print("password should contain atleast one digit")
        return False

    # Check if the password contains at least one special character
    if not re.search(r'[$#@]', password):
        print("password should contain atleast one spacial characater")
        return False

    # If all conditions are met, the password is valid
    return True

# Prompt the user for a password
password = input("Enter a password: ")

# Check the validity of the password
if is_valid_password(password):
    print("Valid Password")
else:
    print("Invalid Password")
