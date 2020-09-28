# Password-Bank
This project is a command-line application that's intended to store and encrypt your social media
passwords for future reference. The application itself will need a username, email, and password 
to be able to use the features. Therefore, multiple users may use this application to store their
social media account information on a device.

## Built With
- Python 3

## Installation
- Download and place the files into it's own folder
- In future iterations of this application, the script may create files that would store encrypted information.
  - After directing command-line into the application's folder, enter "python passwordBank.py"
  
## How To Use
There are two menus in this application.
The first menu is the Main Menu, where the user can register an account, or login to access the Media Menu.
The second menu is the Media Menu, where the user can add, edit, and view their social media information.
Both of these menus prompts the user to enter an acronym associated with an action.

Ex. Main Menu
![Main Menu](https://github.com/jamal-allicock/Password-Bank/blob/master/main_menu.png)
In this case, the user would enter "NEW" to create a new account, "L" to login, etc...

Any password entered must contain
- 8 characters
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
