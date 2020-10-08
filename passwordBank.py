import re
import random

class passwordBank:
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
        self.results = passwordBank.answer_question(self.input_text)

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
    def update_account_password(self):  
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
            for self.domain in passwordBank.VALID_DOMAINS:

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
        
            self.add_account()
         
    
    # Function: add_account
    # Parameter: none
    # Return: none
    # Purpose: add account to platform
    def add_account(self):
        
        self.input_text = "What platform would you like to add an account to: "
        self.results = passwordBank.answer_question(self.input_text)
        if (self.results == "stop" or not self.results): 
            print(self.results)

            return
        else:
            self.platform = self.results.lower()

        if self.platform.casefold() not in self.platform_dict:
            self.setup_account(self.platform,True)


        else:
            print("Adding on to existing platform..")
            for elem in self.platform_dict:
                if elem.casefold() == self.platform.casefold():
                    self.setup_account(self.platform,False)
                    return                 


    def setup_account(self,platform,new):
        self.input_text = "Enter your username for the platform"
        self.results = passwordBank.answer_question(self.input_text)

        if (not self.results):
            return
        else:

            self.username_media = self.results
            print("\n")      
            # Collect password for media platform
            self.platform_password = self.create_password()

            # Store username and password in dictionary key: platform value: [username,password]
            if (new):
                self.temp_key = [self.username_media, self.platform_password]
                self.platform_dict[platform] = [self.temp_key] 
                print(f"{self.platform} has been successfully added.\n")
            else:
                self.temp_key = [self.username_media, self.platform_password]
                self.platform_dict[platform].append(self.temp_key)


                
                
        #{instagram:[['username','password'],[username,user]]}

    # Function: update_platform_username
    # Parameter: none
    # Return: none
    # Purpose: Update platform username
    def update_platform_username(self):
        while True:
            # Collect platform name
            self.input_text = "Enter the platform name of which you choose to change the username"
            self.platform = passwordBank.answer_question(self.input_text)

            # Check if platform exists
            if self.platform not in self.platform_dict:
                print(self.platform + " is not in your bank.\n")
                continue
            if (not self.platform):
                return

            # Collect username
            self.input_text = "Enter your new username"
            self.results = passwordBank.answer_question(self.input_text)

            if (not self.results):
                return
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
        if not self.platform_dict:
            return
        
        # Prints all of the platforms and usernames stored
        self.show_media_platforms()
        
        # Collects platform from user. If the platform doesn't exist, return.
        self.new_platform_pass = input("What is the platform you would like to change the password of?\n")

        # if self.new_platform_pass not in self.platform_dict:
        #     return
        self.user=input("Please enter your username: ")
        for i in range(len(self.platform_dict[self.new_platform_pass])):
        # Updates the previous password
            if self.platform_dict[self.new_platform_pass][i][0]==self.user:
                self.old_pass = self.decrypt_password(self.platform_dict[self.new_platform_pass][i][1])
                print(f"The previous password is {''.join(self.old_pass)}\nPlease enter a new one")
                self.new_pass = self.create_password()
                self.platform_dict[self.platform][i][1] = self.new_pass
                return
        print('You have entered an incorrect password or media.')

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
                self.results = passwordBank.answer_question(self.input_text)

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
            for i in range(len(self.platform_dict[self.key])):
                print(f"\t\t-{str(self.platform_dict.get(self.key)[i][0])}")

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
                self.user = input('Please enter the username of the platform you wish to see: ')
                for i in range(len(self.platform_dict[self.access])):
                    if self.platform_dict[self.access][i][0]==self.user:
                        print(f"The password for {self.access} is : {''.join(self.decrypt_password(self.platform_dict.get(self.access)[i][1]))}\n")
                        return
                print(f'The username \"{self.access}\" is not on file.\n')
            else:  # Check if platform does not exist
                print(f"The platform \"{self.access}\" is not on file.\n")
                return
