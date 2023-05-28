import re
# This program takes a password and checks if it´s a strong password or a weak one


# Create a regex object that contains how a strong password should look like
"""
A strong password has
1. At least 8 Characters
2. Contains both upper and lower case
3. At least one digit
"""
# A password regex can contain any characters
#pw = "hi_fDsgdf-gdf213!"
pw = input("Give a pw: ")
passwordRegex = re.compile(r'[a-zA-Z0-9.,!"§$%&/()=?@€_*#~-]+')
password = passwordRegex.search(pw)
password = password.group(0)

"""
Pseudocode:
Make a function take an argument which is the password
Setup 4 variables that take boolean values we will change them to either "True" or "False"
Set all of them to False initially
longEnoughPw, hasDigitInPw, hasUpperCaseInPw, hasLowerCaseInPw are the variables
First check len(password) to see if the password is 8 chars long
if its over 8 then set longEnoughPw to True otherwise False
Second and Third are done with a for loop
for loop through all the different characters of the password
take the len(password) for the loop
with the individual characters if they are a digit then set hasDigitInPw to True
with the individual characters if they have a uppercase letter set hasUpperCaseInPw to True
with the individual characters if they have a lowercase letter set hasLowerCaseInPw to True
If all boolean variables are True then its a strong password
If one boolean variable is False then its a weak password
"""
# Make a function that checks if a password is a strong password or not
def strongPasswordChecker(password):
    longEnoughPw = False
    hasDigitInPw = False
    hasUpperCaseInPw = False
    hasLowerCaseInPw = False
    hasSpecialCharackter = False
    special_characters = "!@  # $%^&*()-+?_=,<>/"

    if len(password) >= 8:
        longEnoughPw = True

    for i,char in enumerate(password):
        if char.isupper():
            hasUpperCaseInPw = True
        elif char.islower():
            hasLowerCaseInPw = True
        elif char.isnumeric():
            hasDigitInPw = True
        elif char in special_characters:
            hasSpecialCharackter = True

    if longEnoughPw == True and hasDigitInPw == True and hasUpperCaseInPw == True and hasLowerCaseInPw == True and \
            hasSpecialCharackter == True:

        return print("This is a strong password!")
    else:
        return print("This is a weak password please make a stronger one!")

strongPasswordChecker(password)