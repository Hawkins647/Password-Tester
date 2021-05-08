import hashlib
from urllib.request import urlopen


class PasswordCracker:

    def __init__(self, word_list_url):
        self.word_list_url = word_list_url
        self.word_list = self.comprehend_word_list().decode("UTF-8")
        self.guess_pass_list = self.word_list.split("\n")

        self.user_choice = ""
        while self.user_choice != "2":
            print("Please make a selection: ")
            print("1: Check a password")
            print("2: Quit")
            self.user_choice = input("Input your choice here: ")

            if self.user_choice == "1":
                password = input("Please enter your password: ")
                password = self.hash_password(password)
                self.bruteforce(self.guess_pass_list, password)

            if self.user_choice == "2":
                exit()

    def comprehend_word_list(self):
        try:
            word_list = urlopen(self.word_list_url).read()
            return word_list

        except Exception as error:
            print("An error occured whilst reading the list: " + str(error))

    def hash_password(self, password):
        hashed_pass = hashlib.sha1(password.encode())
        return hashed_pass.hexdigest()

    def bruteforce(self, guesspasswordlist, actual_password_hash):
        for guess_password in guesspasswordlist:
            print(guess_password)
            print(hash(guess_password))
            if hash(guess_password) == actual_password_hash:
                print("Hey! your password is: ", guess_password, " I would recommend you change this.\n")
                break

        print("I couldn't get your password. Good job!\n")


test = PasswordCracker('https://raw.githubusercontent.com/berandal666/Passwords/master/10_million_password_list_top_1000000.txt')


# import hashlib
# from urllib.request import urlopen
#
# def readwordlist(url):
#     try:
#         wordlistfile = urlopen(url).read()
#     except Exception as e:
#         print("Hey there was some error while reading the wordlist, error:", e)
#         exit()
#     return wordlistfile
#
#
# def hash(wordlistpassword):
#     result = hashlib.sha1(wordlistpassword.encode())
#     return result.hexdigest()
#
#
# def bruteforce(guesspasswordlist, actual_password_hash):
#     for guess_password in guesspasswordlist:
#         if hash(guess_password) == actual_password_hash:
#             print("Hey! your password is:", guess_password,
#                   "\n please change this, it was really easy to guess it (:")
#             # If the password is found then it will terminate the script here
#             exit()
#
# ############# append the below code ################
#
# url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
# actual_password = 'henry'
# actual_password_hash = hash(actual_password)
#
# wordlist = readwordlist(url).decode('UTF-8')
# guesspasswordlist = wordlist.split('\n')
#
# # Running the Brute Force attack
# bruteforce(guesspasswordlist, actual_password_hash)
#
# # It would be executed if your password was not there in the wordlist
# print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")