import datetime
import time
import winsound
import tkinter as tk

def set_alarm():
    alarm_time = entry.get()
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        label.config(text="Invalid time format. Use HH:MM")
    else:
        label.config(text="Alarm set for " + alarm_time)
        alarm(alarm_time)

def alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            label.config(text="Wake up!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Play a sound file
            break
        time.sleep(1)  # Wait for 1 second before checking again

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

root.mainloop()
