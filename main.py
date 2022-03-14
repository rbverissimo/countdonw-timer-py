import threading
import time
import tkinter as tk
from win10toast import ToastNotifier

# from playsound import playsound

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("460x220") #the size of the main window object
        self.root.title("Pomodoro Timer") #name of the timer

        #creating the widgets

        #the entry placeholder:
        #this line defines the user entry "space" of the software
        self.time_entry = tk.Entry(self.root, font=("Helvetica", 30))
        #this next line draws the user interface
        self.time_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        #the start button :
        self.start_button = tk.Button(self.root, font=("Helvetica", 30), text="Start", command=self.start_thread)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)

        #the stop button :
        self.stop_button = tk.Button(self.root, font=("Helvetica", 30), text="Stop", command=self.stop)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)

        #the label that shows the countdown
        self.time_label = tk.Label(self.root, font=("Helvetica", 30),text="Time: 00:00:00")
        self.time_label.grid(row=2, column=2, columnspan=2,  padx=5, pady=5)

        self.stop_loop = False

        self.root.mainloop()



