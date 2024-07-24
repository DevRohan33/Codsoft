import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Listbox, messagebox
import sqlite3 as sql
from PIL import Image, ImageTk
import sys
from datetime import datetime

def add_task():
    task = task_field.get()
    if task != "":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        the_cursor.execute('insert into tasks (title, timestamp) values (?, ?)', (task, current_time))
        the_connection.commit()
        tasks.append((the_cursor.lastrowid, task, current_time))
        list_update()
        task_field.delete(0, tk.END)
    else:
        print("The task cannot be empty")

def delete_task():
    try:
        task_info = task_listbox.get(tk.ACTIVE)
        task_id = int(task_info.split(".")[0])
        task_to_delete = next(task for task in tasks if task[0] == task_id)
        tasks.remove(task_to_delete)
        the_cursor.execute('delete from tasks where id = ?', (task_id,))
        the_connection.commit()
        reassign_ids()
        list_update()
    except Exception as e:
        print("The task cannot be deleted:", e)

def delete_all_tasks():
    response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all tasks?")
    if response:
        global tasks
        tasks = []
        list_update()
        the_cursor.execute('delete from tasks')
        the_connection.commit()

def reassign_ids():
    for new_id, task in enumerate(tasks, start=1):
        old_id, title, timestamp = task
        tasks[new_id-1] = (new_id, title, timestamp)
        the_cursor.execute('update tasks set id = ? where id = ?', (new_id, old_id))
    the_connection.commit()

def close():
    root.destroy()

def retrieve_database():
    while tasks:
        tasks.pop()
    for row in the_cursor.execute('select id, title, timestamp from tasks'):
        tasks.append((row[0], row[1], row[2]))

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert(tk.END, f"{task[0]}. {task[1]} (added on {task[2]})")

def clear_list():
    task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("665x400+550+250")
    root.resizable(0, 0)

    image_path = "C:/Users/User/Desktop/Programming/Internship/To-do-list/Task 1/bg.jpg"

    try:
        # Load the background image
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((665, 400), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        root.destroy()
        sys.exit(1)

    canvas = tk.Canvas(root, width=665, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    task_label = Label(root, text="Enter the Task Title:", font=("Arial", "14", "bold"), background="#1c0f47", foreground="#05d7ff")
    canvas.create_window(350, 30, window=task_label)

    task_field = Entry(root, font=("Arial", "14"), width=42, foreground="black", background="white")
    canvas.create_window(350, 70, window=task_field)

    add_button = Button(root, text="Add", width=12, bg='#b5321f', font=("arial", "14", "bold"), command=add_task)
    del_button = Button(root, text="Remove", width=12, bg='#b5321f', font=("arial", "14", "bold"), command=delete_task)
    del_all_button = Button(root, text="Delete All", width=12, font=("arial", "14", "bold"), bg='#b5321f', command=delete_all_tasks)
    exit_button = Button(
        root,
        background="#020f12",
        foreground="#05d7ff",
        activebackground="#65e7ff",
        activeforeground="#050505",
        highlightthickness=0,
        highlightbackground="#05d7ff",
        highlightcolor="#65e7ff",
        width=12,
        cursor='hand2',
        text="Close",
        font=("arial", "16", "bold"),
        command=close)

    def bt_enter(event):
        exit_button.config(highlightbackground='#05d7ff')
    def bt_leave(event):
        exit_button.config(highlightbackground='red')

    exit_button.bind("<Enter>", bt_enter)
    exit_button.bind("<Leave>", bt_leave)

    canvas.create_window(100, 110, window=add_button)
    canvas.create_window(330, 110, window=del_button)
    canvas.create_window(560, 110, window=del_all_button)
    canvas.create_window(335, 350, window=exit_button)

    task_listbox = Listbox(root, width=70, height=9, font="bold", selectmode='SINGLE',
                           background="WHITE", foreground="BLACK", selectbackground="#FF8C00", selectforeground="BLACK")
    canvas.create_window(335, 220, window=task_listbox)

    the_connection = sql.connect('store.db')
    the_cursor = the_connection.cursor()

    # Drop the existing table if it exists
    the_cursor.execute('drop table if exists tasks')

    # Create a new table with the correct schema
    the_cursor.execute('create table if not exists tasks (id integer primary key, title text, timestamp text)')

    tasks = []

    retrieve_database()
    list_update()

    canvas.image = bg_photo

    root.mainloop()

    the_connection.commit()
    the_cursor.close()
