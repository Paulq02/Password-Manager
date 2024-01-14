
from tkinter import *

screen = Tk()
screen.minsize(width=500, height=400)
screen.title("Password Generator")
screen.config(background="white")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #



my_canvas = Canvas(width=300, height=300, background="white",highlightbackground="white")
my_canvas.place(x=150, y=1)

logo = PhotoImage(file="/home/paulq02/Desktop/password-manager-start/logo.png")
my_canvas.create_image(120,120,image=logo)


web_label = Label(text="Website:", background="white")
web_label.place(x=30, y=220)

web_entry = Entry(width=35, highlightcolor="blue")
web_entry.place(x=120, y=220)


email_label = Label(text="Email/Username:", background="white")
email_label.place(x=5, y=250)

email_entry = Entry(width=35, highlightcolor="blue")
email_entry.place(x=120, y=250)

password_label = Label(text="Password:", background="white")
password_label.place(x=30, y=280)

password_entry = Entry(width=15, highlightcolor="blue")
password_entry.place(x=120, y=280)

gen_button = Button(text="Generate Password", bg="white", width=16, pady=1, activebackground="white")
gen_button.place(x=250, y=280)


add_button = Button(text="Add", width=32, bg="white", activebackground="white", pady=1)
add_button.place(x=120, y=310)






















screen.mainloop()