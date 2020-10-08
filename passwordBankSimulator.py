import passwordBank as pb

# Function: createNewUser
# Parameter: None
# Return: None
# Purpose: Create new user and add it to the database
def create_new_user():
    # Collect name from user
    name = None
    while not name:
        input_text = "Enter your name"
        results = pb.passwordBank.answer_question(input_text)
        name = results
        if (not results):
            return

    # Loops through the user database to check if the entered username exists already
    while True:
        set = True
        username = input("\nEnter username: ")
        for item in user_database:
            if(item.username == username):
                set = False
                print("This username already exist!\n")
                break
        if (set):
            break

    # Add user to database
    newUser = pb.passwordBank(name, username)
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
        if new_username == "stop":
            return

        # Loops through the function to chech if the username already exists
        for i in user_database:
            if i.username == new_username:
                print("This username has been used before, please enter a new username\n")
                error = False
                break
        if not error:
            continue

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
    result = pb.passwordBank.answer_question(None)
    answer = result
    if not answer:
        return False

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
        elif choice == "exit" or choice == "Exit":
            return
        else:
            print("Please enter a valid input!\n>>")

def media_menu(user):
    while True:
        print("\nMEDIA MENU\n_______________________________________________\nEnter the acroynm associated with the option:\n")
        print("""\t-Add Platform (ADDP)\n\t-Add Account(ADDA)\n\t-Delete Platform(DELP)\n\t-View Accounts(VIEW)
        -Access Password(ACCP)\n\t-Update Platform Password(UPP)\n\t-Update Platform Username(UPU)
        -Settings(SET)\n\t-Log Out(LO)\n""")
        choice = input(">> ")
        
        if choice =="addp" or choice =="ADDP":
            user.add_media_platform()
        elif choice =="adda" or choice =="ADDA":
            user.add_account()
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
            if not result:
                return
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
        if not user_logged_in:
            continue
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

