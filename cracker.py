"""NOTE: This code is heavily taken from https://workshops.hackclub.com/passwordcracker/ - this helped me a lot with
understanding how this can be done, all credit goes to them (:"""

import hashlib
from urllib.request import urlopen


def readwordlist(url):
    try:
        # Get the contents of the wordlist through the urlopen function
        wordlistfile = urlopen(url).read()
    except Exception as error:
        print("Hey there was some error while reading the wordlist, error:", error)
        return None

    # return wordlistfile, decoded in UTF-8 to make it readable
    return wordlistfile.decode("UTF-8")


def hash_password(password: str):
    # hash the given password using the sha1 function
    result = hashlib.sha1(password.encode())
    # return the result in hex format
    return result.hexdigest()


def bruteforce(guesspasswordlist, hashed_pass):
    # Iterate through the password list
    for guess_password in guesspasswordlist:
        # Check to see if the current password hashed is the same as the hash of the user's password
        if hash_password(guess_password) == hashed_pass:
            print("Hey! your password is: ", f"{guess_password},", "I would recommend changing this.")

            # If the password is found, then we will terminate the script here
            exit()


# The list of passwords that you want to check against
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'

# The password that you want to check against
actual_password = 'henry1'

# Hash the password using our function
actual_password_hash = hash_password(actual_password)

# Turn the password string into a list, seperated by newline characters
guesspasswordlist = readwordlist(url).split('\n')

# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)

# It would be executed if your password was not there in the wordlist
print("Password not found in wordlist. Well done.")
