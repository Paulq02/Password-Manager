from tkinter import *

screen = Tk()

screen.title("Password Generator")
screen.config(background="white", padx=50, pady=50)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    web_info = web_entry.get()
    email_info = email_entry.get()
    password_info = password_entry.get()
    my_data = [web_info, email_info, password_info]
    for info in my_data:
        file = open("saved_info.txt", "a")
        file.write(info + " | ")
        
        


        

# ---------------------------- UI SETUP ------------------------------- #
logo = PhotoImage(file="/home/paulq02/Desktop/Password-Manager/logo.png")

my_canvas = Canvas(height=200, width=200, bg="white", highlightbackground="white")
my_canvas.grid(row=0, column=1)

my_canvas.create_image(125,100, image=logo)

web_label = Label(text="Website:", background="white")
web_label.grid(row=1, column=0)

web_entry = Entry(width=43, highlightcolor="blue")
web_entry.grid(row=1, column=1, columnspan=2)


email_label = Label(text="Email/Username:", background="white")
email_label.grid(row=2, column=0)


email_entry = Entry(width=43, highlightcolor="blue")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Paulq10@gmail.com")

password_label = Label(text="Password:", background="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=24, highlightcolor="blue")
password_entry.place(x=119, y=248)

gen_pass_button = Button(background="white", text="Generate Password", pady=0, width=15)
gen_pass_button.grid(row=3, column=2, padx=4)


add_button = Button(text="Add", background="white", width=40, pady=0, command=save_info)
add_button.grid(row=4,column=1, columnspan=2)






screen.mainloop()