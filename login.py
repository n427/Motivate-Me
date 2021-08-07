import tkinter as tk
from tkinter import PhotoImage
from ctypes import windll

''' Page Styling '''
# Initialize sizes
HEIGHT = 1668
WIDTH = 2388
root = tk.Tk()
root.title("Motivate Me!")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = "#FFFFFF")
canvas.pack()
takefocus=False

frame = tk.Frame(root, bg = "#FFFFFF")
frame.place(relx = 0.5, rely = 0.05, relheight = 0.85, relwidth = 0.9, anchor = "n")
windll.shcore.SetProcessDpiAwareness(1)

# Insert Background
login_img = PhotoImage(file = "login_background.png")      
login_bg = tk.Label(frame, image = login_img, bg = "white")
login_bg.place(relx = 0.5, anchor = "n") 


''' Register '''
# Set Fields and Labels
register_username_label = tk.Label(frame, text = "Username:", font = ("Verdana", "35"), bg = "white")
register_username_label.place(rely = 0.3, relx = 0.2, anchor = "n")

register_username_entry = tk.Entry(frame, justify = "center", font = ("Verdana", "25"), width = 18)
register_username_entry.place(rely = 0.37, relx = 0.23, anchor = "n")

register_password_label = tk.Label(frame, text = "Password:", font = ("Verdana", "35"), bg = "white")
register_password_label.place(rely = 0.45, relx = 0.2, anchor = "n")

register_password_entry = tk.Entry(frame, justify = "center", font = ("Verdana", "25"), width = 18, show = "*")
register_password_entry.place(rely = 0.52, relx = 0.23, anchor = "n")

# Register Function
user = " "
def createaccount():
    global user
    user = register_username_entry.get()
    password = register_password_entry.get()
    account = open("users.txt", "a")
    account.write(user + " : ")
    account.write(password + "\n")
    open(user + "_stats.txt", "x")
    open(user + "_goals.txt", "x")
    open(user + "_timetable.txt", "x")
    print(user)
    root.destroy()
    return user
    

register_button = tk.Button(frame, text = "Register", font =("Verdana", "25"), bg = "white", command = createaccount, width = 15)
register_button.place(relx = 0.14, rely = 0.62)


''' Login '''
# Set Fields and Labels
username_label = tk.Label(frame, text = "Username:", font = ("Verdana", "35"), bg = "white")
username_label.place(rely = 0.3, relx = 0.74, anchor = "n")

username_entry = tk.Entry(frame, justify = "center", font = ("Verdana", "25"), width = 18)
username_entry.place(rely = 0.37, relx = 0.77, anchor = "n")

password_label = tk.Label(frame, text = "Password:", font = ("Verdana", "35"), bg = "white")
password_label.place(rely = 0.45, relx = 0.74, anchor = "n")

password_entry = tk.Entry(frame, justify = "center", font = ("Verdana", "25"), width = 18, show = "*")
password_entry.place(rely = 0.52, relx = 0.77, anchor = "n")

# Login Function
user = " "
users = open("users.txt", "r").read()
def login():
    global user
    user = username_entry.get()
    if username_entry.get() and password_entry.get() in users:  
        print(user)
        root.destroy()
    else:
        print("Wrong username / password")
    return user

login_button = tk.Button(frame, text = "Login", font = ("Verdana", "25"), bg = "white", command = login, width = 15)
login_button.place(relx = 0.68, rely = 0.62)


root.mainloop()