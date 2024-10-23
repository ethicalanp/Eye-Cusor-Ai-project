import tkinter as tk
import threading
import Eye_Crusor

tracking = False

def start_tracking():
    global tracking
    tracking = True
    Eye_Crusor.start_tracking()

def stop_tracking():
    global tracking
    tracking = False
    Eye_Crusor.stop_tracking()

def start_tracking_thread():
    tracking_thread = threading.Thread(target=start_tracking)
    tracking_thread.start()

root = tk.Tk()
root.title("Eye Tracker Control")

start_button = tk.Button(root, text="Start Tracking", command=start_tracking_thread)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Tracking", command=stop_tracking)
stop_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()