# Password-Bank
This project is a command-line application that's intended to store and encrypt your social media
passwords for future reference. The application itself will need a username, email, and password 
to be able to use the features.

## Built With
- Python 3

## Installation
- Download and place the files into it's own folder
- In future iterations of this application, the script may create files that would store encrypted information.
  - After directing command-line into the application's folder, enter "python passwordBank.py"
  
## How To Use
This application has a variety of menus in which it prompts the user to enter an acronym associated with an action.
Ex. Main Menu
- Login (L)
- Forgot Password (FP)
- Create an account (NEW)
- Exit (EXIT)

In this case, the user would enter "NEW" to create a new account, "L" to login, etc...

The password entered must contain
- At least 8 characters long
- At least 1 Uppercase letter
- At least 1 lower case letter
- At least 1 number
- At least 1 special character ("!", "@", "$", "&", "*", "_", or ".")

The email must have one of the following domains
- gmail.com
- yahoo.com
- yahoo.ca 
- live.com
- outlook.com
- hotmail.com

## Visuals
![What it would look like in the command-line](https://github.com/jamal-allicock/Password-Bank/blob/master/menus.png)
![The menu to add social media platforms](https://github.com/jamal-allicock/Password-Bank/blob/master/media_menu.png)
