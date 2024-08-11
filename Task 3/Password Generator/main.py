#this code for codsoft internship task -- Password Generate by SK Rohan Parveag
#______________________________________________________________________________#



import random
import string
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

# Colors
bg_color = "#ecf0f1"  
accent_color = "#16a085" 
name_color = "#9534c0" 
text_color = "#2c3e50"  
button_color = "#1abc9c"  
hover_color = "#149174"  
border_color = "#e74c3c"  

# Root window
root = Tk()
root.title('Password Generator')
root.geometry('400x400')
root.configure(bg=bg_color)

# Main frame
frame_main = Frame(root, width=400, height=120, bg=bg_color)
frame_main.grid(row=0, column=0)

# Box frame
frame_box = Frame(root, width=400, height=280, bg=bg_color)
frame_box.grid(row=1, column=0)

# Logo
logo = Image.open('C:/Users/User/Desktop/Programming/Internship/CodSoft/Task 3/Password Generator/icon_password.png')  # Adjust path
logo = logo.resize((40, 40))
logo = ImageTk.PhotoImage(logo)

app_logo = Label(frame_main, image=logo, compound=LEFT, padx=10, bg=bg_color)
app_logo.place(x=50, y=10)

# App Name
app_name = Label(frame_main, text="Password Generator", font=('Fantasy', 17, 'bold'), bg=bg_color, fg=name_color)
app_name.place(x=100, y=20)

# Border
app_border = Label(frame_main, bg=border_color, width=500, height=1)
app_border.place(x=0, y=70)

# Password Length
Label(frame_main, text='Password Length', font=('Helvetica', 13), bg=bg_color, fg=text_color).place(x=20, y=95)
var = IntVar(value=8)
Spinbox(frame_main, from_=4, to=20, textvariable=var, width=5, font=('Helvetica', 13)).place(x=160, y=95)

# Strength Indicator
strength_label = Label(frame_main, text='Strength: Weak', font=('Helvetica', 13), bg=bg_color, fg=text_color)
strength_label.place(x=250, y=95)

# Password Display
app_password = Label(frame_box, text='- - -', width=30, height=2, relief='solid', font=('Helvetica', 14), bg=bg_color, fg=text_color)
app_password.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

# Functions for password strength
def update_strength(password):
    length = len(password)
    if length < 6:
        strength_label.config(text='Strength: Weak', fg='#e74c3c')
    elif length < 10:
        strength_label.config(text='Strength: Medium', fg='#f39c12')
    else:
        strength_label.config(text='Strength: Strong', fg='#2ecc71')
#Function for password generate
def generate_password():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special_chars = "!@#$%^&*()"

    selected_chars = ""
    if first_state.get():
        selected_chars += uppercase
    if second_state.get():
        selected_chars += lowercase
    if third_state.get():
        selected_chars += numbers
    if fourth_state.get():
        selected_chars += special_chars

    length = var.get()
    if selected_chars:
        password = "".join(random.sample(selected_chars * length, length))
        app_password.config(text=password)
        update_strength(password)
    else:
        messagebox.showwarning("Selection Error", "Please select at least one character set!")
#Function for copy
def copy_password():
    password = app_password.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Buttons
button_generate = Button(frame_box, text='Generate Password', command=generate_password, bg=button_color, fg=bg_color, font=('Helvetica', 12), activebackground=hover_color, relief=FLAT)
button_generate.grid(row=1, column=0, pady=10, padx=10)

button_copy = Button(frame_box, text='Copy', command=copy_password, bg=button_color, fg=bg_color,font=('Helvetica', 12), activebackground=hover_color, relief=FLAT)
button_copy.grid(row=1, column=1, pady=10, padx=10)

# Checkbuttons
Label(frame_box, text="Include:", font=('Helvetica', 12), bg=bg_color, fg=text_color).grid(row=2, column=0, columnspan=2)

first_state = BooleanVar()
second_state = BooleanVar()
third_state = BooleanVar()
fourth_state = BooleanVar()

Checkbutton(frame_box, text="Uppercase Letters (ABCD..Z)", variable=first_state, bg=bg_color, fg=text_color,
            font=('Helvetica', 10)).grid(row=3, column=0, sticky=W, padx=20, pady=2)
Checkbutton(frame_box, text="Lowercase Letters  (abcd..z)", variable=second_state, bg=bg_color, fg=text_color,
            font=('Helvetica', 10)).grid(row=4, column=0, sticky=W, padx=20, pady=2)
Checkbutton(frame_box, text="Numbers  (012..9)", variable=third_state, bg=bg_color, fg=text_color,
            font=('Helvetica', 10)).grid(row=5, column=0, sticky=W, padx=20, pady=2)
Checkbutton(frame_box, text="Special Characters  (@#$..*)", variable=fourth_state, bg=bg_color, fg=text_color,
            font=('Helvetica', 10)).grid(row=6, column=0, sticky=W, padx=20, pady=2)

root.mainloop()
