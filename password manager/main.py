from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    def swap(string):
        return string[-1:] + string[1:-1] + string[:1]

    password_string = ""
    for letter in range(0, nr_letters):
        x = random.randint(0, len(letters) - 1)
        password_string += letters[x]
    for symbol in range(0, nr_symbols):
        x = random.randint(0, len(symbols) - 1)
        password_string += symbols[x]
    for number in range(0, nr_numbers):
        x = random.randint(0, len(numbers) - 1)
        password_string += numbers[x]
    final_password = swap(password_string)
    password.insert(END, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_value():
    website_value = website.get()
    password_value = password.get()

    if website_value == '' or password_value == '':
        messagebox.showinfo(message='Invalid password or website')
    elif len(password_value) < 8:
        messagebox.showinfo(title='Strong Password', message='Please use a stronger password')

    else:
        box = messagebox.askyesno(title='Double Check',
                                  message=f'Website: {website_value}\n Password: {password_value}\nConfirm?')
        if box:
            with open('passwords.txt', mode='a') as f:
                data = [website_value + ' | ' + 'vladelinschii05@gmail.com' + ' | ' + password_value + '\n']
                f.writelines(data)
                password.delete(0, END)
                website.delete(0, END)
                website.focus()
                messagebox.showinfo(title='Credentials Saved', message='Saved Successfully!')


# ---------------------------- UI SETUP ------------------------------- #
MAIN_COLOR = '#EFF5F5'
FONT = ('Avenir', 14)
TEXT_COLOR = '#5F8D4E'
ENTRY_COLOR = '#4E6C50'

root = Tk()
root.title('Password Manager')
root.geometry('600x500')
root.config(background=MAIN_COLOR, pady=20, padx=20)

canvas = Canvas(width=200, height=200, bg=MAIN_COLOR, highlightthickness=0)
photo = PhotoImage(file='logo.png')  # Saving the image into a variable

canvas.create_image(100, 100, image=photo)  # Creating the canvas
canvas.grid(column=1, row=0)

# ---Creating the inputs

# Website
website_text = Label(text='Website: ', font=FONT, fg=TEXT_COLOR, bg=MAIN_COLOR)
website_text.grid(row=1, column=0)

# Email/username
username_text = Label(text='Email/username: ', font=FONT, fg=TEXT_COLOR, bg=MAIN_COLOR)
username_text.grid(row=2, column=0)

# Password
password_text = Label(text='Password: ', font=FONT, fg=TEXT_COLOR, bg=MAIN_COLOR)
password_text.grid(row=3, column=0)

# ---Entries

# Website
website = Entry(bg=ENTRY_COLOR, fg='white', highlightthickness=0, width=40)
website.grid(row=1, column=1, columnspan=2, pady=5)
website.focus()  # Focusing on the website when we run the app

# Username/email
username = Entry(bg=ENTRY_COLOR, fg='white', highlightthickness=0, width=40)
username.grid(row=2, column=1, columnspan=2, pady=5)
username.insert(END, 'vladelinschii05@gmail.com')  # Making the mail as constant

# Password
password = Entry(bg=ENTRY_COLOR, fg='white', highlightthickness=0, width=22)
password.grid(row=3, column=1, pady=5)

# ---Buttons

# Password
generate_password = Button(text='Generate Password', font=FONT, highlightthickness=0, bd=0, command=generate_password)
generate_password.grid(row=3, column=2)

# Add
add_button = Button(text='Save Password', font=FONT, width=44, highlightthickness=0, bd=0, command=get_value)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

root.mainloop()
