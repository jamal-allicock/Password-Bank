# Create passwordBank class
import re
import random
import time


class PasswordBank:
    # local variables
    VALID_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com",
                     "hotmail.com", "yahoo.ca", "live.com"]

    # Keys
    alpha_key, num_key = "", ""
    ALPHA = list("abcdefghijklmnopqrstuvwxyz")
    NUM_SPECIAL = list("0123456789!@$&*_.")
    MAIN_KEY = ALPHA + NUM_SPECIAL

    # user passwordsBank

    # constructor

    def __init__(self, name_of_person, username_account):
        self.name = name_of_person
        self.unique_key = self.create_unique_key()
        self.username = self.create_username(username_account)
        self.password = self.create_password()
        self.email = self.create_email()
        self.platform_dict={}



    def __repr__(self):
        # print account information
        self.show_name()
        self.show_username()
        self.show_email()
        self.show_media_platforms()
        return f"{self.username}"

    @classmethod
    # str1, str2, option, option_var,input_text):
    def answer_question(cls, input_text):
        while True:
            # Prompts input text if necessary
            if input_text:
                cls.option = input(f"Enter \"stop\" to quit\n{input_text}: ")
                if(cls.option == "stop") or (cls.option == "STOP"):
                    print("No changes have been made.\n")
                    return False
                cls.answer = input(f"Is {cls.option} correct(Y/N)?: ")
            # Get user response and return appropriate value
            else:
                cls.answer = input("")
            if (cls.answer == "Y" or cls.answer == "y"):
                return cls.option
            elif(cls.answer == "N" or cls.answer == "n"):
                print("Try again!")
                continue
            elif(cls.answer == "stop" or cls.answer == "STOP"):
                print("No changes have been made.\n")
                return False
            else:
                print(f"{cls.answer} is an invalid input. Please try again.")
                continue

    # Function: update_account_name
    # Parameter: none
    # Return: none
    # Purpose: Update name of user
    def update_account_name(self):
        self.previous = self.name
        print(f"The previous name on this account was {self.name}.")

        self.input_text = "Enter updated name"
        self.results = PasswordBank.answer_question(self.input_text)

        if (not self.results): return
        self.name = self.results

    # Function: create_password
    # Parameter: none
    # Return: none
    # Purpose: checks to make sure the password the user inputs is valid
    def create_password(self, check_previous_input=None):
        # Must have at least one capital, lowercase, special character
        self.error = 1
        self.check_previous_password = check_previous_input
        if self.check_previous_password:
            self.check_previous_password = ''.join(
                self.decrypt_password(check_previous_input))

        # Uses success as counter to count errors in password
        while (self.error > 0):
            self.error = 0
            self.password = input("Enter a password: ")

            # Prints out exact error
            if((len(self.password) < 8) or (re.search("[a-z]", self.password) == None) or (re.search("[A-Z]", self.password) == None) or (re.search("[0-9]", self.password) == None) or (re.search("[!@$&*_.]", self.password) == None)):
                self.error += 1
                if (len(self.password) < 8): print("Your password MUST be atleast 8 characters!")
                if (re.search("[a-z]", self.password) == None):  print("Your password MUST contain at least 1 lower case letter!")
                if (re.search("[A-Z]", self.password) == None):  print("Your password MUST contain at least 1 upper case letter!")
                if (re.search("[0-9]", self.password) == None):  print("Your password MUST contain at least 1 number!")
                if (re.search("[!@$&*_.]", self.password) == None):  print("Your password MUST contain at least 1 special character! (!, @, $, &, *,_ , or .)")
                print("\n")
            
            # Checks if each character in password is NOT in MAIN_KEY
            for self.char in self.password:
                if self.char not in self.MAIN_KEY and not (self.char).isalpha():
                    print("Your password MUST contain a VALID special character! (!, @, $, &, *,_ , or .)\n")
                    self.error += 1
                    break

        # If there is no previous password or the previous password is not the same as the old -> set password
        if not(self.check_previous_password) or (self.check_previous_password != self.password):
            print("Your password is valid!\n")
            # print(''.join(self.password) + ": Original Password")
            self.password = self.encrypt_password(self.password)
            # print(''.join(self.password) + ": Encrypted Password\n")
         
            return self.password
        # Check if previous password = new password
        elif (self.check_previous_password == self.password): return False
    
          
    # Function: update_account_password
    # Parameter: None
    # Return: None
    # Purpose: change account password
    def update_account_password(self):  # ISSUE IT'S STUCK IN A LOOP
        self.updated_password = None
        self.previous = ''.join(self.password)

        print(f"The previous password on this account was {''.join(self.decrypt_password(self.password))}. Set up your new password.")

        # Prompt user to create new password -> Make sure it's not the same as previous
        while True:
            self.password = self.create_password(self.previous)
            if(not self.password):
                print("Please do not use previous passwords.")
                continue
            elif(self.password != self.previous):
                self.updated_password = ''.join(self.decrypt_password(self.password))
                print(f"The account password has been successfully updated.\n")# from {''.join(self.decrypt_password(self.previous))} to {self.updated_password}.")
                return

    # Function: create_unique_key
    # Parameter: None
    # Return: List unique_key
    # Purpose: Creates a key for the user (object)

    def create_unique_key(self):
        self.alpha_key = self.ALPHA
        self.alpha_key = list(self.alpha_key)

        self.num_key = self.NUM_SPECIAL
        self.num_key = list(self.num_key)

        # Shuffles list elements
        random.shuffle(self.alpha_key)
        random.shuffle(self.num_key)

        self.unique_key = self.alpha_key + self.num_key
        return self.unique_key

    # Function: decrypt_Password
    # Parameter: password
    # Return : list password
    # Purpose : decrypt password for when user needs to see password
    def decrypt_password(self, password):
        # print(f"Before: {password}")
        self.index = 0
        self.new_password = list(password)

        for self.char in self.new_password:
            self.key_index = self.unique_key.index(self.char.lower())
            if (self.char.isalpha() and self.char.islower()) or (not self.char.isalpha()):
                self.new_password[self.index] = self.MAIN_KEY[self.key_index]
            elif self.char.isalpha() and self.char.isupper():
                self.new_password[self.index] = self.MAIN_KEY[self.key_index].upper()

            self.index += 1
        return self.new_password

    # Function: encryptPassword
    # Parameter: password
    # Return : list password
    # Purpose : Encrypt password for user protection
    def encrypt_password(self, password):
        # Find the index where character in password occurs in the MAIN_KEY and the swap with the uniquekey
        lower, upper, other = False,False,False
   
        self.temp_password = list(self.password)
        self.new_password = ""
        
        for self.item in self.temp_password:
            # Find the index where character in password occurs
            #       - in the MAIN_KEY and the swap with the uniquekey according to the flags
            self.index = self.MAIN_KEY.index(self.item.lower())
            self.unique_key_index = self.unique_key[self.index]
            
            if self.item.isupper():
                self.new_password += (self.unique_key_index).upper()
            elif self.item.islower(): 
                self.new_password += (self.unique_key_index).lower()
            else: 
                self.new_password += self.unique_key_index

        return (self.new_password)


    # Function : create_username
    # Parameter : none
    # return: none
    # Purpose: To create user following (no spaces in username no special characters)
    def create_username(self, username_input):
        self.success = 1  # error counter
        self.username_input = username_input

        while (self.success > 0):
            self.success = 0
            if (not self.username_input):
                self.success += 1
                print("Please enter text!\n")
             
            else:
                # If username contains a space or is not a number or letter ask user to enter it again
                # . and _ are allowed
                for self.item in self.username_input:
                    if (self.item == '.') or (self.item == '_') or (self.item.isalnum()): continue
                    else:
                        self.success += 1
                        break

                if self.success == 0:
                    print(f"{self.username_input} is a valid username!\n")
                    return self.username_input

            self.username_input = input(f"The username you have entered ({self.username_input}) is invalid.\nPlease enter a valid username (No special characters or spaces): ")

    # Function: createEmail
    # Parameter: None
    # Return: email
    # Purpose: To get the email from the user and make sure its a valid input
    def create_email(self):
        # while loop that will continue forever until the user enters a valid email
        # once a valid email is entered, it will return the email, cutting the while loop
        while True:
            self.email = input("Please enter a valid email: ")
            for self.domain in PasswordBank.VALID_DOMAINS:

                # If there is a space in the entered email, break the for loop to ask for input again
                if ' ' in self.email: break

                # If the selected domain is in the email and it is at the end of the email string,
                    # return the email to end the while loop
                if (self.domain in self.email) and ((len(self.email) - self.email.index(self.domain)) == (len(self.domain))):
                    if self.email[0] == '@': break
                    return self.email

    # Function: addMediaPlatform
    # Parameter: None
    # Return: None
    # Purpose: Add a platform the users bank
    def add_media_platform(self):
        self.agree = False
        self.answer = ""

        while True:
            # Allow user to stop adding platforms
            print("Press any key to continue...")
            print("Enter \"stop\" if you want to stop adding new platforms")
            self.end = input("Answer : ")
            if self.end == "stop":
                print("\n")
                break

            self.input_text = "Enter the name of the platform"
            self.results = PasswordBank.answer_question(self.input_text)
            if (self.results == "stop" or not self.results): return
            else:self.platform = self.results
            print("\n")
            self.input_text = "Enter your username for the platform"
            self.results = PasswordBank.answer_question(self.input_text)
            if (not self.results): return
            else: self.username_media = self.results
            print("\n")
            # Collect password for media platform
            self.platform_password = self.create_password()

            # Store username and password in dictionary key: platform value: [username,password]
            self.temp_key = [self.username_media, self.platform_password]
            self.platform_dict[self.platform] = self.temp_key
            print(f"{self.platform} has been successfully added.\n")

    # Function: update_platform_username
    # Parameter: none
    # Return: none
    # Purpose: Update platform username
    def update_platform_username(self):
        while True:
            # Collect platform name
            self.input_text = "Enter the platform name of which you choose to change the username"
            self.platform = PasswordBank.answer_question(self.input_text)

            # Check if platform exists
            if self.platform not in self.platform_dict:
                print(self.platform + " is not in your bank.\n")
                continue
            if (not self.platform): return

            # Collect username
            self.input_text = "Enter your new username"
            self.results = PasswordBank.answer_question(self.input_text)

            if (not self.results): return
            if (self.username_media == self.results):
                print("Please do not use previous usernames.\n")
                continue
            break

        self.username_media = self.results
        self.platform_dict[self.platform] = [self.username_media, self.platform_dict.get(self.platform)[1]]

        print(f"Your new {str(self.platform)} username has been chanegd to {str(self.platform_dict.get(self.platform)[0])}\n")
        print(self.platform_dict.get(self.platform))
    
    # Function: update_platform_password
    # Parameter: None
    # Return: None
    # Purpose: Update platform password
    def update_platform_password(self):
        #if there are no platforms, return nothing
        if not self.platform_dict: return
        
        # Prints all of the platforms and usernames stored
        self.show_media_platforms()
        
        # Collects platform from user. If the platform doesn't exist, return.
        self.new_platform_pass = input("What is the platform you would like to change the password of?\n")

        if self.new_platform_pass not in self.platform_dict: return

        # Updates the previous password
        self.old_pass = self.decrypt_password(self.platform_dict[self.new_platform_pass][1])
        print(f"The previous password is {''.join(self.old_pass)}\nPlease enter a new one")
        self.new_pass = self.create_password()
        self.platform_dict[self.platform][1] = self.new_pass

    # Function:remove_platform
    # Parameter: None
    # Return: None
    # Purpose: Remove the stored username and password for the requested media platform
    def remove_platform(self):
        # Displays the accounts for each platform
        self.show_media_platforms()

        while True:
            # asks the user if they want to stop removing platforms
            print("Enter \"stop\" if you want to stop removing platforms")
            self.platform_removed = input( "Enter the name of the platform you would like to remove: ")
          
            if self.platform_removed == "stop":  break
            if self.platform_removed not in self.platform_dict:
                print(self.platform_removed + " is not in your bank.\n")
                continue

            # asks user if they want to delete the platform and will break the while loop if they dont
            while self.platform_removed in self.platform_dict:
                print(f"The following is your username for {self.platform_removed}: {self.platform_dict.get(self.platform_removed)[0]}")

                self.input_text = "Do you stll wish to delete this platform from your database? (Y/N)"
                self.results = PasswordBank.answer_question(self.input_text)

                if(not self.results): return
                del self.platform_dict[self.platform_removed]
                print(f"You have deleted {self.platform_removed} from the database!\n")
                break
            # self.show_media_platforms()

    # Display Functions
    def show_name(self): print(f"Name: {self.name}")

    def show_email(self): print(f"Email: {self.email}")

    def show_username(self): print(f"Username: {self.username}")

    def show_media_platforms(self):
        if not(len(self.platform_dict)):
            print("There are no platforms\n.")
            return
        print("Platforms in your Bank:")
        for self.key in self.platform_dict:
            print(f"\t~{self.key}")
            print(f"\t\t-{str(self.platform_dict.get(self.key)[0])}")

    # Function: showMediaPlatformPassword
    # Parameter: None
    # Return: None
    # Purpose: Reveal a password for platform
    def show_media_platform_password(self):
        # Checks if dictionary is empty
        if not len(self.platform_dict):
            print("There are no platforms.\n")
            return

        while True:
            self.show_media_platforms()  # shows list of platforms
            self.access = input("Enter the platform you would like to see the password for: ")
            # Check if platform exists  -> print password
            if self.access in self.platform_dict:
                print(f"The password for {self.access} is : {''.join(self.decrypt_password(self.platform_dict.get(self.access)[1]))}\n")
                return
            else:  # Check if platform does not exist
                print(f"The platform \"{self.access}\" in not on file.\n")
                return


# Function: createNewUser
# Parameter: None
# Return: None
# Purpose: Create new user and add it to the database
def create_new_user():
    # Collect name from user
    name = None
    while not name:
        input_text = "Enter your name"
        results = PasswordBank.answer_question(input_text)
        name = results
        if (not results): return

    # Loops through the user database to check if the entered username exists already
    while True:
        set = True
        username = input("\nEnter username: ")
        for item in user_database:
            if(item.username == username):
                set = False
                print("This username already exist!\n")
                break
        if (set): break

    # Add user to database
    newUser = PasswordBank(name, username)
    user_database.append(newUser)
    print("Account successfully created!\n")

# Function: changeUsername
# Parameter: None
# Return: the username of the person logged in!
# Purpose: To change the username of the person logged in

def change_username():
    current_Username = user_logged_in.username
    while True:
        # Asks the user for an new username input and will cut the function if the user enters stop
        error = True
        new_username = input(
            "Enter \"stop\" to not change username \nPlease enter your new username:  ")
        if new_username == "stop": return

        # Loops through the function to chech if the username already exists
        for i in user_database:
            if i.username == new_username:
                print("This username has been used before, please enter a new username\n")
                error = False
                break
        if not error: continue

        new_username = user_logged_in.create_username(new_username)

        # changes the username of the person logged in to the entered new username
        user_logged_in.username = new_username
        return user_logged_in.username



# Function: login
# Parameter: None
# Return: item Object
# Purpose: Login user into database
def login():
    print("LOG IN PAGE... \n")
    # Check if username and password match and exist
    while True:
        # Collects username and password
        username = input("Please enter a username: ")
        password = input("Enter password: ")

        # Searches for object by using username and decrypted password
        for item in user_database:
            print("\n")
            if(item.username == username and ''.join(item.decrypt_password(item.password)) == password):
                # Return object in variable once found
                print("Logging in...")
                print(f"Welcome {item.name}!\n")
                return item

        #Checks if user would like to leave
        while True:
            results = input("Incorrect Username or Password. Would you like to return to the main menu? (Y/N): ")
            if results == "n" or results == "N": break
            elif  results == "y" or results == "Y": return False
            else: print("Please enter a valid input.\n")


# Function: delete_account
# Parameter: user Object
# Return: Boolean
# Purpose: To delete user from database
def delete_account(user):
    # Check if user would like to delete account
    print("Would you like to delete your account (Y/N)?")
    result = PasswordBank.answer_question(None)
    answer = result
    if not answer: return False

    # Search for account and delete it from database
    for i in range(len(user_database)):
        # print(id(user_database[i]))
        # print(id(user))
        if id(user_database[i]) == id(user):
            del user_database[i]
            return True

# Function: forgot_assword
# Parameter: None
# Return: None
# Purpose: Remind user of lost password
def forgot_password():
    # prints passsword based on email or username
    user_input = input("Enter your Email or Username to change your password: ")

    for user in user_database:
        if user.username == user_input or user.email == user_input:
            print(f"{user.name}, your account has been found!\n")
            found = ''.join(user.decrypt_password(user.password))
            print(f"Your password is : {found}.")
            return
        else:
            print("You have entered an invalid email or username.\n")
            break

user_database = []
def settings(user):
    while True:
        print("\nSETTINGS\n_______________________________________________\nEnter the acroynm associated with the option:\n")
        print("""\t-Update Account Name (UPAN)\n\t-Update Account Username (UPAU)\n\t-Update Account Password (UPAP)
        -Delete Account(DELA)\n\t-Exit Settings(EXIT)\n""")
        choice = input(">>")

        if choice== "UPAN" or choice =="upan":
            user.update_account_name()
        elif choice == "upau" or choice == "UPAU":
            change_username()
        elif choice == "upap" or choice == "UPAP":
            user.update_account_password()
        elif choice == "dela" or choice == "DELA":
            delete = delete_account(user)
            if delete:
                user_logged_in = None
                return False
        elif choice == "exit" or choice == "EXIT":
            return True
        else:
            print("Please enter a valid input!\n>>")

def media_menu(user):
    while True:
        print("\nMEDIA MENU\n_______________________________________________\nEnter the acroynm associated with the option:\n")
        print("""\t-Add Platform (ADDP)\n\t-Delete Platform(DELP)\n\t-View Accounts(VIEW)
        -Access Password(ACCP)\n\t-Update Platform Password(UPP)\n\t-Update Platform Username(UPU)
        -Settings(SET)\n\t-Log Out(LO)\n""")
        choice = input(">> ")
        
        if choice =="addp" or choice =="ADDP":
            user.add_media_platform()
        elif choice =="delp" or choice =="DELP":
            user.remove_platform()
        elif choice == "view" or choice =="VIEW":
            user.show_media_platforms()
        elif choice == "accp" or choice =="ACCP":
            user.show_media_platform_password()
        elif choice == "upp" or choice =="UPP":
            user.update_platform_password()
        elif choice == "upu" or choice =="UPU":
            user.update_platform_username()
        elif choice == "set" or choice == "SET":
            result = settings(user)
            if not result: return
        elif choice == "lo" or choice == "LO":
            print("Logging out...\n")
            return
        else:
            print("Please enter a valid input!\n >>")

#Main Menu
while True:
    user_logged_in=None  
    print("MAIN MENU\n_______________________________________________\nEnter the acroynm associated with the options:\n")
    print("\t-Login (L)\n\t-Forgot Password (FP)\n\t-Create an account (NEW)\n\t-Exit (EXIT)\n")
    choice = input(">> ")
    if choice =="L" or choice =="l":  
        user_logged_in = login()
        if not user_logged_in: continue
        # print(f"User Database > {user_database}")
        media_menu(user_logged_in) 
    elif choice ==  "FP" or choice == "fp":
        forgot_password()
    elif choice=="NEW" or choice =="new":
        create_new_user()
    elif choice == "exit" or choice == "EXIT":
        print("Thank you for using our program!!")
        break
    else:
        print("Please enter a valid input!\n >>")

























































# Main Menu (An actual function)

# Create an account - Done
#    Store all users of the passwordbank application in a list
#       -Make sure username is unique
#       createnewuser()
# Login - DONE
#   login()
#        search if username and password is tied to an object with the class then we return it
#        Now your logged in (media)
#         we with a for loop....
#           once it's found right?
#           userLoggedIN = item <- object
#
#        M E D I A
#        View all accounts - DONE
#        Update platform password - DONE
#        Delete Platform  - DONE
#           - no platform return
#        Add Platform - DONE
#        Access password - DONE
#           - no platform return
#        Update platform password - DONE
#           - no platform return
#        Update platform username - DONE
#           - no platform return
#        Settings (actual account)
#            Print info Collected - (email, name, username, accounts)
#            Update account name - DONE
#            Update account username -  90% DONE
#            Update account password - DONE
#            Delete account - DONE
#        Log out - SIMPLE
# FORGET PASSWORD - DONE
#       userDatabase = [object, object,......]
#       input string (email/username)
#       check user or email
#       search through UserDatabase look if the username or email exist
#       return list[0].decrypt(password)
#       for item in userDatabase:
#           if (item.password == ____ || item.email == _____):
#               found retuRn password

