from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip
import json

BACKGROUND = "#204985"
FOREGROUND = "#ffffff"
FONT_LOOK = "Rubik", 12, "bold"
EMAIL = "skaftisveins@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(6, 8))]
    password_numbers = [choice(numbers)for _ in range(randint(1, 2))]
    password_symbols = [choice(symbols)for _ in range(randint(1, 2))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # Put password into the clipboard, ready for copy and paste
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():  # Function to save password
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    def write_or_update_json_file(mode):
        """Simple function to write or update existing data"""
        with open("data.json", "w") as data_file:
            json.dump(mode, data_file, indent=4)

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Whoops!", message="Please don't leave any fields empty!")
        return None

    is_ok = messagebox.askokcancel(
        title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                print(f"Saving password for: {website}")
                existing_data = json.load(data_file)  # Reading existing_data
                if website in existing_data:
                    update = messagebox.askyesno("Warning", f"There is already a password saved for {website}.\n"
                                                 f"Would you like to overwrite?")
                    if update:
                        existing_data[website]["password"] = password
                        existing_data[website]["email"] = email
                    else:
                        return
                else:
                    existing_data.update(new_data)

        except FileNotFoundError as error_message:
            print(
                f"File Not Found...{error_message},\nCreating new data.json file...")
            write_or_update_json_file(new_data)

        else:
            # Updating existing_data with new_data
            existing_data.update(new_data)
            write_or_update_json_file(existing_data)

        finally:
            # Clear all fields in entry inputs after Add button is pressed
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        is_ok = False

# ---------------------------- FIND PASSWORD ------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in existing_data:
            email = existing_data[website]["email"]
            password = existing_data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background=BACKGROUND)

canvas = Canvas(width=200, height=200,
                background=BACKGROUND, highlightthickness=0)

lock_img = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", background=BACKGROUND,
                      foreground=FOREGROUND, font=(FONT_LOOK))
website_label.grid(column=0, row=1)
username_label = Label(text="Email: ", background=BACKGROUND,
                       foreground=FOREGROUND, font=(FONT_LOOK))
username_label.grid(column=0, row=2)
password_label = Label(text="Password: ", background=BACKGROUND,
                       foreground=FOREGROUND, font=(FONT_LOOK))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW", pady=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email = email_entry.insert(0, EMAIL)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
search_website = Button(text="Search", command=find_password)
search_website.grid(column=2, row=1, sticky="EW")
gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(column=2, row=3)
add_password = Button(text="Add", width=36, command=save)
add_password.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
