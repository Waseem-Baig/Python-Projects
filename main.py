from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) > 0:
        if len(email) > 0:
            if len(password) > 0:
                answer = messagebox.askyesno(title="Confirm", message=f"These are the entered details\n"
                                                                      f"Website: {website}\n"
                                                                      f"Email: {email}\n"
                                                                      f"Password: {password}")
                if answer:
                    try:
                        with open("data.json", "r") as data:
                            load_data = json.load(data)
                    except FileNotFoundError:
                        with open("data.json", "w") as data:
                            json.dump(new_data, data, indent=4)
                    else:
                        load_data.update(new_data)
                        with open("data.json", "w") as data:
                            json.dump(load_data, data, indent=4)
                    finally:
                        website_input.delete(0, END)
                        email_input.delete(0, END)
                        password_input.delete(0, END)

                else:
                    website_input.delete(0, END)
                    email_input.delete(0, END)
                    password_input.delete(0, END)
            else:
                messagebox.showwarning(title="Password", message="Password field can not be empty.")
        else:
            messagebox.showwarning(title="Email", message="Email field can not be empty.")
    else:
        messagebox.showwarning(title="Website", message="Website field can not be empty.")


def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Website not found", message=f"{website} has not uploaded")


# ---------------------------- UI SETUP ------------------------------- #\
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:", font=("Arial", 12, "normal"))
website_label.config(padx=20, pady=10)
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.config(width=41)
website_input.grid(column=1, row=1)
website_input.focus()

website_search_button = Button(text="Search", command=search)
website_search_button.config(width=14, bg="white", highlightthickness=0)
website_search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", font=("Arial", 12, "normal"))
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.config(width=60)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 12, "normal"))
password_label.config(padx=20, pady=10)
password_label.grid(column=0, row=3)

password_input = Entry(width=41)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generate)
generate_button.config(width=14, bg="white", highlightthickness=0)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_password)
add_button.config(width=50, bg="white", highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
