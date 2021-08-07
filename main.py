import tkinter as tk
from tkinter import StringVar, mainloop, ttk, PhotoImage, messagebox
from ctypes import windll
import time
from pygame import mixer
from datetime import date
import os
import fileinput
from login import *

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
frame.place(relx = 0.5, rely = 0.05, anchor = "n")
windll.shcore.SetProcessDpiAwareness(1)

# Create tabs
s = ttk.Style()
s.configure('TNotebook.Tab', font=("Verdana",'20') )
tabs = ttk.Notebook(root)
tabs.place(relx = 0.05, rely = 0.05, relheight = 0.85, relwidth = 0.9)

timer = tk.Frame(tabs, frame)
goals = tk.Frame(tabs, frame)
timetable = tk.Frame(tabs, frame)
music = tk.Frame(tabs, frame)
reset = tk.Frame(tabs, frame)

timer.place()
goals.place()
timetable.place()
music.place()
reset.place()

tabs.add(timer, text = "           \n          Pomodoro          \n             ")
tabs.add(goals, text = "          \n            Goals           \n           ")
tabs.add(timetable, text = "          \n          Timetable         \n           ")
tabs.add(music, text = "          \n            Music             \n          ")
tabs.add(reset, text = "          \n            Reset             \n          ")

# Insert backgrounds
timer_img = PhotoImage(file = "timer_background.png")      
timer_bg = tk.Label(timer, image = timer_img, bg = "white")
timer_bg.place(relx = 0.5, anchor = "n") 

goals_img = PhotoImage(file = "goals_background.png")  
goals_bg = tk.Label(goals, image = goals_img, bg = "white")
goals_bg.place(relx = 0.5, anchor = "n") 

music_img = PhotoImage(file = "music_background.png")  
music_bg = tk.Label(music, image = music_img, bg = "white")
music_bg.place(relx = 0.5, anchor = "n") 

timetable_img = PhotoImage(file = "timetable_background.png")  
timetable_bg = tk.Label(timetable, image = timetable_img, bg = "white")
timetable_bg.place(relx = 0.5, anchor = "n") 


''' Timer Page '''
# Define variables
work_hour = StringVar()
work_minute = StringVar()
work_second = StringVar()
work_hour.set("00")
work_minute.set("00")
work_second.set("00")

break_hour = StringVar()
break_minute = StringVar()
break_second = StringVar()
break_hour.set("00")
break_minute.set("00")
break_second.set("00")

# Placing work timer and labels
work_hour_entry = tk.Entry(timer, textvariable = work_hour, width = 4, font = ("Verdana", "58"), justify = "center")
work_hour_entry.place(relx = 0.35, rely = 0.3, anchor = "n")

colon_label = tk.Label(timer, text = ":", font = ("Verdana", "40"), bg = "White")
colon_label.place(relx = 0.425, rely = 0.31, anchor = "n")

work_minute_entry = tk.Entry(timer, justify = "center", textvariable = work_minute, width = 4, font = ("Verdana", "58"))
work_minute_entry.place(relx = 0.5, rely = 0.3, anchor = "n")

colon_label = tk.Label(timer, text = ":", font = ("Verdana", "40"), bg = "White")
colon_label.place(relx = 0.575, rely = 0.31, anchor = "n")

work_second_entry = tk.Entry(timer, justify = "center", textvariable = work_second, width = 4, font = ("Verdana", "58"))
work_second_entry.place(relx = 0.65, rely = 0.3, anchor = "n")

# Placing break timer and labels
break_hour_entry = tk.Entry(timer, justify = "center", textvariable = break_hour, width = 4, font = ("Verdana", "58"))
break_hour_entry.place(relx = 0.35, rely = 0.5, anchor = "n")

colon_label = tk.Label(timer, text = ":", font = ("Verdana", "40"), bg = "White")
colon_label.place(relx = 0.425, rely = 0.51, anchor = "n")

break_minute_entry = tk.Entry(timer, justify = "center", textvariable = break_minute, width = 4, font = ("Verdana", "58"))
break_minute_entry.place(relx = 0.5, rely = 0.5, anchor = "n")

colon_label = tk.Label(timer, text = ":", font = ("Verdana", "40"), bg = "White")
colon_label.place(relx = 0.575, rely = 0.51, anchor = "n")

break_second_entry = tk.Entry(timer, justify = "center", textvariable = break_second, width = 4, font = ("Verdana", "58"))
break_second_entry.place(relx = 0.65, rely = 0.5, anchor = "n")

# Function to start break
def work_break():
    temp = int(break_hour.get())*3600 + int(break_minute.get())*60 + int(break_second.get())
    # Update timer
    while temp > -1:
        mins,secs = divmod(temp,60)
        hours=0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        break_hour.set("{0:2d}".format(hours))
        break_minute.set("{0:2d}".format(mins))
        break_second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)

        # Okcancel Messagebox 
        if (temp == 0):
            messagebox.askokcancel("Motivate Me!", "Keep on going!")
            work_hour.set("00")
            work_minute.set("00")
            work_second.set("00")
            break_hour.set("00")
            break_minute.set("00")
            break_second.set("00")   
        temp -= 1

# Function to start timer 
def start_timer():
    stats = open(user + "_stats.txt", "a")

    # Add stats to txt file
    stats.write(work_hour.get() + " hours " + work_minute.get() + " minutes " + work_second.get() + " seconds \n")

    temp = int(work_hour.get())*3600 + int(work_minute.get())*60 + int(work_second.get())
    # Update timer
    while temp > -1:
        mins,secs = divmod(temp,60)
        hours=0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        work_hour.set("{0:2d}".format(hours))
        work_minute.set("{0:2d}".format(mins))
        work_second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)

        # Yes/No messagebox to start break timer
        if (temp == 0):
            continue_timer = messagebox.askquestion("Motivate Me!", "Good job! You worked well :) \n" + "Would you like to continue to break?")
            if continue_timer == "yes":
                work_break()
            else:
                work_hour.set("00")
                work_minute.set("00")
                work_second.set("00")
                break_hour.set("00")
                break_minute.set("00")
                break_second.set("00")  
        temp -= 1

work_button = tk.Button(timer, text = "Start Working!", font = ("Verdana", "25"), bg = "white", command = start_timer)
work_button.place(relx = 0.5, rely = 0.65, anchor = "n")


''' Goals Page '''
# Check if the goals file is empty
if os.path.getsize(user + "_goals.txt") == 0:
    # Morning Entries
    morning_entry_1 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    morning_entry_1.place(relx = 0.2, rely = 0.15, anchor = "n")

    morning_entry_2 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    morning_entry_2.place(relx = 0.5, rely = 0.2, anchor = "n")

    morning_entry_3 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    morning_entry_3.place(relx = 0.8, rely = 0.15, anchor = "n")

    # Afternoon Entries
    afternoon_entry_1 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    afternoon_entry_1.place(relx = 0.2, rely = 0.5, anchor = "n")

    afternoon_entry_2 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    afternoon_entry_2.place(relx = 0.5, rely = 0.5, anchor = "n")

    afternoon_entry_3 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    afternoon_entry_3.place(relx = 0.8, rely = 0.5, anchor = "n")

    # Evening Entries
    evening_entry_1 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    evening_entry_1.place(relx = 0.2, rely = 0.8, anchor = "n")

    evening_entry_2 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    evening_entry_2.place(relx = 0.5, rely = 0.75, anchor = "n")

    evening_entry_3 = tk.Entry(goals, justify = "center", width = 15, font = ("Verdana", "25"), borderwidth=2, relief="groove")
    evening_entry_3.place(relx = 0.8, rely = 0.8, anchor = "n")

    # Save the goals to txt file
    def save_goals():
        goals_file = open(user + "_goals.txt", "a")
        goals_file.write(morning_entry_1.get() + "\n")
        goals_file.write(morning_entry_2.get() + "\n")
        goals_file.write(morning_entry_3.get() + "\n")
        goals_file.write(afternoon_entry_1.get() + "\n")
        goals_file.write(afternoon_entry_2.get() + "\n")
        goals_file.write(afternoon_entry_3.get() + "\n")
        goals_file.write(evening_entry_1.get() + "\n")
        goals_file.write(evening_entry_2.get() + "\n")
        goals_file.write(evening_entry_3.get() + "\n\n")

        goals_file.close()

        # Show saved values
        morning_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = morning_entry_1.get(), bg = "white", borderwidth=2, relief="groove")
        morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n")

        # Show labels
        def morning_1_complete(): 
            morning_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = morning_entry_1.get(), bg = "white", borderwidth=2, relief="groove")
            morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n")
            
            if len(morning_label_1.cget("text")) != 0:
                morning_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Great start!", bg = "white", borderwidth=2, relief="groove")
                morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n") 

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[0] = "Great Start!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else: 
                morning_label_1 = tk.Label(goals, width = 15, text = "No Goal Set", font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[0] = "Great Start!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()  

        morning_button_1 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = morning_1_complete)
        morning_button_1.place(relx = 0.2, rely = 0.2, anchor = "n") 

        morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = morning_entry_2.get(), bg = "white", borderwidth=2, relief="groove")
        morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")

        def morning_2_complete():
            morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = morning_entry_2.get(), bg = "white", borderwidth=2, relief="groove")
            morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")

            if len(morning_label_2.cget("text")) != 0:
                morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Nice!", bg = "white", borderwidth=2, relief="groove")
                morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[1] = "Nice!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else:
                morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "No Goal Set", bg = "white", borderwidth=2, relief="groove")
                morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")

        morning_button_2 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = morning_2_complete)
        morning_button_2.place(relx = 0.5, rely = 0.25, anchor = "n")
        

        morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = morning_entry_3.get(), bg = "white", borderwidth=2, relief="groove")
        morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")
        
        def morning_3_complete(): 
            morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = morning_entry_3.get(), bg = "white", borderwidth=2, relief="groove")
            morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")
        
            if len(morning_label_3.cget("text")) != 0:
                morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Morning Done!", bg = "white", borderwidth=2, relief="groove")
                morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[2] = "Morning Done!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else:
                morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")
        
        morning_button_3 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = morning_3_complete)
        morning_button_3.place(relx = 0.8, rely = 0.2, anchor = "n")

        afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = afternoon_entry_1.get(), bg = "white", borderwidth=2, relief="groove")
        afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")
        
        def afternoon_1_complete(): 
            afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = afternoon_entry_1.get(), bg = "white", borderwidth=2, relief="groove")
            afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")

            if len(afternoon_label_1.cget("text")) != 0:
                afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Amazing!", bg = "white", borderwidth=2, relief="groove")
                afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[3] = "Amazing!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else: 
                afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Amazing!", bg = "white", borderwidth=2, relief="groove")
                afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")
            
        afternoon_button_1 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = afternoon_1_complete)
        afternoon_button_1.place(relx = 0.2, rely = 0.55, anchor = "n")
            
        afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = afternoon_entry_2.get(), bg = "white", borderwidth=2, relief="groove")
        afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")

        def afternoon_2_complete(): 
            afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = afternoon_entry_2.get(), bg = "white", borderwidth=2, relief="groove")
            afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")

            if len(afternoon_label_2.cget("text")) != 0:
                afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Halfway Done!", bg = "white", borderwidth=2, relief="groove")
                afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[4] = "Halfway Done!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else:
                afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")
        
        afternoon_button_2 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = afternoon_2_complete)
        afternoon_button_2.place(relx = 0.5, rely = 0.55, anchor = "n")

        afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = afternoon_entry_3.get(), bg = "white", borderwidth=2, relief="groove")
        afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")
        
        def afternoon_3_complete():
            afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = afternoon_entry_3.get(), bg = "white", borderwidth=2, relief="groove")
            afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")

            if len(afternoon_label_3.cget("text")) != 0:
                afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Great Work!", bg = "white", borderwidth=2, relief="groove")
                afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[5] = "Great Work!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else:
                afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")
        
        afternoon_button_3 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = afternoon_3_complete)
        afternoon_button_3.place(relx = 0.8, rely = 0.55, anchor = "n")

        evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = evening_entry_1.get(), bg = "white", borderwidth=2, relief="groove")
        evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")
        
        def evening_1_complete():
            evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = evening_entry_1.get(), bg = "white", borderwidth=2, relief="groove")
            evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")

            if len(evening_label_1.cget("text")) != 0:
                evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Sooo Close!", bg = "white", borderwidth=2, relief="groove")
                evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[6] = "Sooo Close!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else:
                evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")
        
        evening_button_1 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = evening_1_complete)
        evening_button_1.place(relx = 0.2, rely = 0.85, anchor = "n")

        evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = evening_entry_2.get(), bg = "white", borderwidth=2, relief="groove")
        evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")
        
        def evening_2_complete():
            evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = evening_entry_2.get(), bg = "white", borderwidth=2, relief="groove")
            evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")

            if len(evening_label_2.cget("text")) != 0:
                evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Day's Ending!", bg = "white", borderwidth=2, relief="groove")
                evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[7] = "Day's Ending!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else:
                evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")
        
        evening_button_2 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = evening_2_complete)
        evening_button_2.place(relx = 0.5, rely = 0.8, anchor = "n")

        evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = evening_entry_3.get(), bg = "white", borderwidth=2, relief="groove")
        evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")
        
        def evening_3_complete():
            evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = evening_entry_3.get(), bg = "white", borderwidth=2, relief="groove")
            evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")

            if len(evening_label_3.cget("text")) != 0:
                evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Finished!", bg = "white", borderwidth=2, relief="groove")
                evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[8] = "Finished!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else:
                evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")
        
        evening_button_3 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = evening_3_complete)
        evening_button_3.place(relx = 0.8, rely = 0.85, anchor = "n")

    save_goals_button = tk.Button(goals, text = "Save", command = lambda : [save_goals(), save_goals_button.destroy()], bg = "white", font = ("Verdana", "20"))
    save_goals_button.place(relx = 0.9, rely = 0.9, anchor = "n")

# If there's already values in the txt file    
else:
    # Read lines
    with open(user + "_goals.txt", "r") as fp:
        lines = fp.readlines()
        
        # Show labels
        morning_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[0].strip(), bg = "white", borderwidth=2, relief="groove")
        morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n")
        
        # Show finished message
        def morning_1_complete(): 
            morning_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[0].strip(), bg = "white", borderwidth=2, relief="groove")
            morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n")
            
            if len(morning_label_1.cget("text")) != 0:
                morning_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Great start!", bg = "white", borderwidth=2, relief="groove")
                morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n") 

                open_file = open(user + "_goals.txt", "r")
                list_of_lines = open_file.readlines()
                list_of_lines[0] = "Great Start!\n"

                open_file = open(user + "_goals.txt", "w")
                open_file.writelines(list_of_lines)
                open_file.close()
            else: 
                morning_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                morning_label_1.place(relx = 0.2, rely = 0.15, anchor = "n")  

        morning_button_1 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = morning_1_complete)
        morning_button_1.place(relx = 0.2, rely = 0.2, anchor = "n") 

        morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[1].strip(), bg = "white", borderwidth=2, relief="groove")
        morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")

        def morning_2_complete():
            morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[1].strip(), bg = "white", borderwidth=2, relief="groove")
            morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")

            if len(morning_label_2.cget("text")) != 0:
                morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Nice!", bg = "white", borderwidth=2, relief="groove")
                morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")
            else:
                morning_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "No Goal Set", bg = "white", borderwidth=2, relief="groove")
                morning_label_2.place(relx = 0.5, rely = 0.2, anchor = "n")

        morning_button_2 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = morning_2_complete)
        morning_button_2.place(relx = 0.5, rely = 0.25, anchor = "n")
        

        morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[2].strip(), bg = "white", borderwidth=2, relief="groove")
        morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")
        
        def morning_3_complete(): 
            morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[2].strip(), bg = "white", borderwidth=2, relief="groove")
            morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")
        
            if len(morning_label_3.cget("text")) != 0:
                morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Morning Done!", bg = "white", borderwidth=2, relief="groove")
                morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")
            else:
                morning_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                morning_label_3.place(relx = 0.8, rely = 0.15, anchor = "n")
        
        morning_button_3 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = morning_3_complete)
        morning_button_3.place(relx = 0.8, rely = 0.2, anchor = "n")

        afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[3].strip(), bg = "white", borderwidth=2, relief="groove")
        afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")
        
        def afternoon_1_complete(): 
            afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[3].strip(), bg = "white", borderwidth=2, relief="groove")
            afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")

            if len(afternoon_label_1.cget("text")) != 0:
                afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Amazing!", bg = "white", borderwidth=2, relief="groove")
                afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")
            else: 
                afternoon_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Amazing!", bg = "white", borderwidth=2, relief="groove")
                afternoon_label_1.place(relx = 0.2, rely = 0.5, anchor = "n")
            
        afternoon_button_1 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = afternoon_1_complete)
        afternoon_button_1.place(relx = 0.2, rely = 0.55, anchor = "n")
            
        afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[4].strip(), bg = "white", borderwidth=2, relief="groove")
        afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")

        def afternoon_2_complete(): 
            afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[4].strip(), bg = "white", borderwidth=2, relief="groove")
            afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")

            if len(afternoon_label_2.cget("text")) != 0:
                afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Halfway Done!", bg = "white", borderwidth=2, relief="groove")
                afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")
            else:
                afternoon_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                afternoon_label_2.place(relx = 0.5, rely = 0.5, anchor = "n")
        
        afternoon_button_2 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = afternoon_2_complete)
        afternoon_button_2.place(relx = 0.5, rely = 0.55, anchor = "n")

        afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[5].strip(), bg = "white", borderwidth=2, relief="groove")
        afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")
        
        def afternoon_3_complete():
            afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[5].strip(), bg = "white", borderwidth=2, relief="groove")
            afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")

            if len(afternoon_label_3.cget("text")) != 0:
                    afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Great Work!", bg = "white", borderwidth=2, relief="groove")
                    afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")
            else:
                    afternoon_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                    afternoon_label_3.place(relx = 0.8, rely = 0.5, anchor = "n")
        
        afternoon_button_3 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = afternoon_3_complete)
        afternoon_button_3.place(relx = 0.8, rely = 0.55, anchor = "n")

        evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[6].strip(), bg = "white", borderwidth=2, relief="groove")
        evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")
        
        def evening_1_complete():
            evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[6].strip(), bg = "white", borderwidth=2, relief="groove")
            evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")

            if len(evening_label_1.cget("text")) != 0:
                evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Great Work!", bg = "white", borderwidth=2, relief="groove")
                evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")
            else:
                evening_label_1 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                evening_label_1.place(relx = 0.2, rely = 0.8, anchor = "n")
        
        evening_button_1 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = evening_1_complete)
        evening_button_1.place(relx = 0.2, rely = 0.85, anchor = "n")

        evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[7].strip(), bg = "white", borderwidth=2, relief="groove")
        evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")
        
        def evening_2_complete():
            evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[7].strip(), bg = "white", borderwidth=2, relief="groove")
            evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")

            if len(evening_label_2.cget("text")) != 0:
                evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Day's Ending!", bg = "white", borderwidth=2, relief="groove")
                evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")
            else:
                evening_label_2 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                evening_label_2.place(relx = 0.5, rely = 0.75, anchor = "n")
        
        evening_button_2 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = evening_2_complete)
        evening_button_2.place(relx = 0.5, rely = 0.8, anchor = "n")

        evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[8].strip(), bg = "white", borderwidth=2, relief="groove")
        evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")
        
        def evening_3_complete():
            evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = lines[8].strip(), bg = "white", borderwidth=2, relief="groove")
            evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")

            if len(evening_label_3.cget("text")) != 0:
                evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), text = "Finished!", bg = "white", borderwidth=2, relief="groove")
                evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")
            else:
                evening_label_3 = tk.Label(goals, width = 15, font = ("Verdana", "25"), bg = "white", borderwidth=2, relief="groove")
                evening_label_3.place(relx = 0.8, rely = 0.8, anchor = "n")
        
        evening_button_3 = tk.Button(goals, takefocus = False, font = ("Verdana", "20"), text = "☑", bg = "white", command = evening_3_complete)
        evening_button_3.place(relx = 0.8, rely = 0.85, anchor = "n")


''' Timetable '''
# Check if file is empty
if os.path.getsize(user + "_timetable.txt") == 0:
    # Initialize background
    timetable_img = PhotoImage(file = "timetable_background.png")  
    timetable_bg = tk.Label(timetable, image = timetable_img, bg = "white")
    timetable_bg.place(relx = 0.5, anchor = "n") 

    # Entries
    # First Column
    schedule_entry_1 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_1.place(relx = 0.2, rely = 0.1, anchor = "n")

    time_entry_1 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_1.place(relx = 0.155, rely = 0.15, anchor = "n")

    schedule_entry_2 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_2.place(relx = 0.2, rely = 0.27, anchor = "n")

    time_entry_2 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_2.place(relx = 0.155, rely = 0.32, anchor = "n")

    schedule_entry_3 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_3.place(relx = 0.2, rely = 0.44, anchor = "n")

    time_entry_3 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_3.place(relx = 0.155, rely = 0.49, anchor = "n")

    schedule_entry_4 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_4.place(relx = 0.2, rely = 0.61, anchor = "n")

    time_entry_4 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_4.place(relx = 0.155, rely = 0.66, anchor = "n")

    schedule_entry_5 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_5.place(relx = 0.2, rely = 0.78, anchor = "n")

    time_entry_5 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_5.place(relx = 0.155, rely = 0.83, anchor = "n")

    # Second Column
    schedule_entry_6 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_6.place(relx = 0.5, rely = 0.1, anchor = "n")

    time_entry_6 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_6.place(relx = 0.455, rely = 0.15, anchor = "n")

    schedule_entry_7 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_7.place(relx = 0.5, rely = 0.27, anchor = "n")

    time_entry_7 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_7.place(relx = 0.455, rely = 0.32, anchor = "n")

    schedule_entry_8 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_8.place(relx = 0.5, rely = 0.44, anchor = "n")

    time_entry_8 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_8.place(relx = 0.455, rely = 0.49, anchor = "n")

    schedule_entry_9 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_9.place(relx = 0.5, rely = 0.61, anchor = "n")

    time_entry_9 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_9.place(relx = 0.455, rely = 0.66, anchor = "n")

    schedule_entry_10 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_10.place(relx = 0.5, rely = 0.78, anchor = "n")

    time_entry_10 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_10.place(relx = 0.455, rely = 0.83, anchor = "n")

    # Third Column
    schedule_entry_11 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_11.place(relx = 0.8, rely = 0.1, anchor = "n")

    time_entry_11 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_11.place(relx = 0.755, rely = 0.15, anchor = "n")

    schedule_entry_12 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_12.place(relx = 0.8, rely = 0.27, anchor = "n")

    time_entry_12 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_12.place(relx = 0.755, rely = 0.32, anchor = "n")

    schedule_entry_13 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_13.place(relx = 0.8, rely = 0.44, anchor = "n")

    time_entry_13 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_13.place(relx = 0.755, rely = 0.49, anchor = "n")

    schedule_entry_14 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_14.place(relx = 0.8, rely = 0.61, anchor = "n")

    time_entry_14 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_14.place(relx = 0.755, rely = 0.66, anchor = "n")

    schedule_entry_15 = tk.Entry(timetable, justify = "center", width = 15, font = ("Verdana", "25"))
    schedule_entry_15.place(relx = 0.8, rely = 0.78, anchor = "n")

    time_entry_15 = tk.Entry(timetable, justify = "center", width = 7, font = ("Verdana", "20"))
    time_entry_15.place(relx = 0.755, rely = 0.83, anchor = "n")

    # Add values to txt file
    saved_img = PhotoImage(file = "timetable_saved_background.png")
    def save():
        # Initialize new background
        timetable_saved_bg = tk.Label(timetable, image = saved_img, bg = "white")
        timetable_saved_bg.place(relx = 0.5, anchor = "n") 

        timetable_file = open(user + "_timetable.txt", "a")
        timetable_file.write(schedule_entry_1.get() + "\n" + time_entry_1.get() + "\n")
        timetable_file.write(schedule_entry_2.get() + "\n" + time_entry_2.get() + "\n")
        timetable_file.write(schedule_entry_3.get() + "\n" + time_entry_3.get() + "\n")
        timetable_file.write(schedule_entry_4.get() + "\n" + time_entry_4.get() + "\n")
        timetable_file.write(schedule_entry_5.get() + "\n" + time_entry_5.get() + "\n")
        timetable_file.write(schedule_entry_6.get() + "\n" + time_entry_6.get() + "\n")
        timetable_file.write(schedule_entry_7.get() + "\n" + time_entry_7.get() + "\n")
        timetable_file.write(schedule_entry_8.get() + "\n" + time_entry_8.get() + "\n")
        timetable_file.write(schedule_entry_9.get() + "\n" + time_entry_9.get() + "\n")
        timetable_file.write(schedule_entry_10.get() + "\n" + time_entry_10.get() + "\n")
        timetable_file.write(schedule_entry_11.get() + "\n" + time_entry_11.get() + "\n")
        timetable_file.write(schedule_entry_12.get() + "\n" + time_entry_12.get() + "\n")
        timetable_file.write(schedule_entry_13.get() + "\n" + time_entry_13.get() + "\n")
        timetable_file.write(schedule_entry_14.get() + "\n" + time_entry_14.get() + "\n")
        timetable_file.write(schedule_entry_15.get() + "\n" + time_entry_15.get() + "\n\n")

        # First Column
        schedule_label_1 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_1.get() + "\n" + schedule_entry_1.get(), bg = "white")
        schedule_label_1.place(relx = 0.2, rely = 0.1, anchor = "n")

        schedule_label_2 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_2.get() + "\n" + schedule_entry_2.get(), bg = "white")
        schedule_label_2.place(relx = 0.2, rely = 0.28, anchor = "n")

        schedule_label_3 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_3.get() + "\n" + schedule_entry_3.get(), bg = "white")
        schedule_label_3.place(relx = 0.2, rely = 0.44, anchor = "n")

        schedule_label_4 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_4.get() + "\n" + schedule_entry_4.get(), bg = "white")
        schedule_label_4.place(relx = 0.2, rely = 0.61, anchor = "n")

        schedule_label_5 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_5.get() + "\n" + schedule_entry_5.get(), bg = "white")
        schedule_label_5.place(relx = 0.2, rely = 0.78, anchor = "n")

        # Second Column
        schedule_label_6 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_6.get() + "\n" + schedule_entry_6.get(), bg = "white")
        schedule_label_6.place(relx = 0.5, rely = 0.1, anchor = "n")

        schedule_label_7 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_7.get() + "\n" + schedule_entry_7.get(), bg = "white")
        schedule_label_7.place(relx = 0.5, rely = 0.28, anchor = "n")

        schedule_label_8 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_8.get() + "\n" + schedule_entry_8.get(), bg = "white")
        schedule_label_8.place(relx = 0.5, rely = 0.44, anchor = "n")

        schedule_label_9 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_9.get() + "\n" + schedule_entry_9.get(), bg = "white")
        schedule_label_9.place(relx = 0.5, rely = 0.61, anchor = "n")

        schedule_label_10 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_10.get() + "\n" + schedule_entry_10.get(), bg = "white")
        schedule_label_10.place(relx = 0.5, rely = 0.78, anchor = "n")

        # Third Column
        schedule_label_11 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_11.get() + "\n" + schedule_entry_11.get(), bg = "white")
        schedule_label_11.place(relx = 0.8, rely = 0.1, anchor = "n")

        schedule_label_12 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_12.get() + "\n" + schedule_entry_12.get(), bg = "white")
        schedule_label_12.place(relx = 0.8, rely = 0.28, anchor = "n")

        schedule_label_13 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_13.get() + "\n" + schedule_entry_13.get(), bg = "white")
        schedule_label_13.place(relx = 0.8, rely = 0.44, anchor = "n")

        schedule_label_14 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_14.get() + "\n" + schedule_entry_14.get(), bg = "white")
        schedule_label_14.place(relx = 0.8, rely = 0.61, anchor = "n")

        schedule_label_15 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = time_entry_15.get() + "\n" + schedule_entry_15.get(), bg = "white")
        schedule_label_15.place(relx = 0.8, rely = 0.78, anchor = "n")
    
    save_button = tk.Button(timetable, text = "save", command = lambda : [save(), save_button.destroy()], width = 8, bg = "white", font = ("Verdana", 15))
    save_button.place(relx = 0.9, rely = 0.9, anchor = "n")

else:
    # Initialize background
    saved_img = PhotoImage(file = "timetable_saved_background.png")
    timetable_saved_bg = tk.Label(timetable, image = saved_img, bg = "white")
    timetable_saved_bg.place(relx = 0.5, anchor = "n") 

    # Read lines
    with open(user + "_timetable.txt", "r") as fp:
        lines = fp.readlines()
        # Show values from file
        def open_file():
            # First Column
            schedule_label_1 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[1].strip() + "\n" + lines[0].strip(), bg = "white")
            schedule_label_1.place(relx = 0.2, rely = 0.1, anchor = "n")

            schedule_label_2 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[3].strip() + "\n" + lines[2].strip(), bg = "white")
            schedule_label_2.place(relx = 0.2, rely = 0.28, anchor = "n")

            schedule_label_3 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[5].strip() + "\n" + lines[4].strip(), bg = "white")
            schedule_label_3.place(relx = 0.2, rely = 0.44, anchor = "n")

            schedule_label_4 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[7].strip() + "\n" + lines[6].strip(), bg = "white")
            schedule_label_4.place(relx = 0.2, rely = 0.61, anchor = "n")

            schedule_label_5 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[9].strip() + "\n" + lines[8].strip(), bg = "white")
            schedule_label_5.place(relx = 0.2, rely = 0.78, anchor = "n")

            # Second Column
            schedule_label_6 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[11].strip() + "\n" + lines[10].strip(), bg = "white")
            schedule_label_6.place(relx = 0.5, rely = 0.1, anchor = "n")

            schedule_label_7 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[13].strip() + "\n" + lines[12].strip(), bg = "white")
            schedule_label_7.place(relx = 0.5, rely = 0.28, anchor = "n")

            schedule_label_8 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[15].strip() + "\n" + lines[14].strip(), bg = "white")
            schedule_label_8.place(relx = 0.5, rely = 0.44, anchor = "n")

            schedule_label_9 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[17].strip() + "\n" + lines[16].strip(), bg = "white")
            schedule_label_9.place(relx = 0.5, rely = 0.61, anchor = "n")

            schedule_label_10 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[19].strip() + "\n" + lines[18].strip(), bg = "white")
            schedule_label_10.place(relx = 0.5, rely = 0.78, anchor = "n")

            # Third Column
            schedule_label_11 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[21].strip() + "\n" + lines[20].strip(), bg = "white")
            schedule_label_11.place(relx = 0.8, rely = 0.1, anchor = "n")

            schedule_label_12 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[23].strip() + "\n" + lines[22].strip(), bg = "white")
            schedule_label_12.place(relx = 0.8, rely = 0.28, anchor = "n")

            schedule_label_13 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[25].strip() + "\n" + lines[24].strip(), bg = "white")
            schedule_label_13.place(relx = 0.8, rely = 0.44, anchor = "n")

            schedule_label_14 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[27].strip() + "\n" + lines[26].strip(), bg = "white")
            schedule_label_14.place(relx = 0.8, rely = 0.61, anchor = "n")

            schedule_label_15 = tk.Label(timetable, width = 20, height = 3, font = ("Verdana", "25"), text = lines[29].strip() + "\n" + lines[28].strip(), bg = "white")
            schedule_label_15.place(relx = 0.8, rely = 0.78, anchor = "n")

        open_file()


''' Music Page '''
# No-Lyrics Music
def play_lofi():
    mixer.init()
    mixer.music.load("lofi_music.wav")
    mixer.music.play()

    def pause_lofi():
        mixer.music.pause()    
    lofi_pause_button = tk.Button(music, takefocus = False, font = ("Verdana", "25"), text = "Pause", bg = "white", command = pause_lofi)
    lofi_pause_button.place(relx = 0.2, rely = 0.83, anchor = "n")

lofi_img = PhotoImage(file = "lofi_cover.png")  
lofi_bg = tk.Label(music, image = lofi_img, bg = "white")
lofi_bg.place(relx = 0.2, rely = 0.05, anchor = "n") 

lofi_button = tk.Button(music, takefocus = False, font = ("Verdana", "25"), text = "Play", bg = "white", command = play_lofi)
lofi_button.place(relx = 0.2, rely = 0.74, anchor = "n")

# Lyrics Music
def play_lyrics():
    mixer.init()
    mixer.music.load("lyrics_music.wav")
    mixer.music.play()

    def pause_lyrics():
        mixer.music.pause()  
    lofi_pause_button = tk.Button(music, takefocus = False, font = ("Verdana", "25"), text = "Pause", bg = "white", command = pause_lyrics)
    lofi_pause_button.place(relx = 0.8, rely = 0.83, anchor = "n")

lyrics_img = PhotoImage(file = "lyrics_cover.png")
lyrics_bg = tk.Label(music, image = lyrics_img, bg = "white")
lyrics_bg.place(relx = 0.8, rely = 0.05, anchor = "n") 

lyrics_button = tk.Button(music, takefocus = False, font = ("Verdana", "25"), text = "Play", bg = "white", command = play_lyrics)
lyrics_button.place(relx = 0.8, rely = 0.74, anchor = "n")


''' Stats Page '''



''' Run GUI '''
root.mainloop()