# Python-Tkinter-Password-Manager-Day-29
### What I learned: 
Python refactoring imports, tkinter messagebox, pyperclip and using json in Python. Had a lot of fun with this one and been adding couple of features since first version.

![grab-landing-page](https://github.com/skaftisveins/Python-Tkinter-Password-Manager-Day-29/blob/master/demo.gif)
![ScreenShot](https://github.com/skaftisveins/Python-Tkinter-Password-Manager-Day-29/blob/master/screenshot.png)

### Functions and what they do

### generate_password():
Generate password takes random number of picks from a list of letters, numbers and symbols and joins it together. Pyperclip module used to make password ready to go on your copy and paste clipboard, when the button has been clicked.

### save():
Save method writes your info to a data.json if no entry fields are empty.
Added check if website already exists in database, popupbox will give warnning with a Yes or No options to ovwerwrite.
Then it clears the entry fields, if saved successfull!
Wrapped it in a try catch block with except FileNotFoundError, else and finally

### find_password():
Take input from website_entry and check if website exists in data.json.
First time users exception handle added, if no data.json exists.
Show popup message box with website, email and password.
If it does not find a website in data.json, user gets a showinfo messagebox.

Added .gitignore for data.txt and data.json
