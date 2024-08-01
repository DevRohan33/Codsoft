from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)
    screen.update()

root = Tk()
root.text("Calculator")
root.geometry("400x600")
root.configure(bg="black")

# Screen area
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 28 bold", bd=10, relief=SUNKEN, justify=RIGHT, bg="#333", fg="white")
screen.pack(fill=BOTH, ipadx=8, padx=10, pady=10)

# Button frame 
def create_button(frame, text, bg_color, fg_color):
    button = Button(frame, text=text, font="lucida 20 bold", padx=20, pady=20, bg=bg_color, fg=fg_color, relief=FLAT)
    button.pack(side=LEFT, expand=True, fill=BOTH)
    button.bind("<Button-1>", click)
    return button

# Button colors
button_bg_color = "#444"
button_fg_color = "white"
operator_bg_color = "#666"
operator_fg_color = "white"

# Create button frames
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for texts in button_texts:
    f = Frame(root, bg="black")
    f.pack(expand=True, fill=BOTH)
    for text in texts:
        if text in ["+", "-", "*", "/"]:
            create_button(f, text, operator_bg_color, operator_fg_color)
        elif text in ["C", "="]:
            create_button(f, text, "#FF6347", "white")  
        else:
            create_button(f, text, button_bg_color, button_fg_color)

root.mainloop()
