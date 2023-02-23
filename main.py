# python3

import tkinter as tk

# Constants for the dialog box
PINK = "#e2979c"
FONT = ("Courier", 15, "bold")

timer = 60


# Start test: the "start" button disappears, text field activates, timer starts
def start_test():
    start_button.grid_forget()
    entry.config(state="normal")
    start_timer()


# Start the timer and change the label to "Timer"
def start_timer():
    count_down(timer)
    name_label.config(text="Timer:", fg=PINK)


# Count down to 0 and show the results using existing labels
def count_down(count):
    timer_label.config(text=f"{count} seconds", fg=PINK)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Text string being split into a list of separate words
        text = entry.get("1.0", 'end-1c').split(" ")
        entry.config(state="disabled")
        name_label.config(text="Your result:", fg=PINK)
        timer_label.config(text=f"{len(text)} words per minute", fg=PINK)


# App window
window = tk.Tk()
window.title("Typing Speed Test")
window.config(height=150, width=150, pady=20, padx=20)

name_label = tk.Label(text="You will be given a minute to type as many words as you can",
                      fg=PINK,
                      font=FONT)
name_label.grid(column=0, row=0, columnspan=2, pady=5)

timer_label = tk.Label(text="Timer: 60 seconds", fg=PINK, font=FONT)
timer_label.grid(column=0, row=1, columnspan=2, pady=5)

start_button = tk.Button(text="Start test", font=FONT, padx=3, pady=3, command=start_test)
start_button.grid(column=0, row=2, columnspan=2, pady=5)

# Entry is disabled until the user starts the test and the timer goes off
entry = tk.Text(height=10, width=50, state="disabled")
entry.grid(column=0, row=3, columnspan=2, pady=5)

window.mainloop()
