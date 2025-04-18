import os
import time
import subprocess
import threading

# Define the time to lock the system (30 seconds)
lock_duration = 10

# Store the original wallpaper path
original_wallpaper = "<orignal_image_path>"

# Function to lock the system using xtrlock
def lock_system():
    
    # Set the background image using feh
    background_image_path = "<background_image_path>"  # Update with the path to your image
    # Lock the system using xtrlock
    os.system(f"feh -ZFzr {background_image_path} & ")
    os.system(f" xtrlock  -f &")

# Function to display the timer using zenity
def display_timer():
    #subprocess.Popen(["zenity", "--info", "--text", "Press OK to unlock.", "--title", "Timer"])
    subprocess.Popen(["zenity", "--info", "--text=Press OK to unlock.", "--title=Timer"])

# Create a thread to update the timer
timer_thread = threading.Thread(target=display_timer)

# Lock the system
lock_system()

# Start the timer thread
timer_thread.start()

# Wait for the timer thread to finish
timer_thread.join()

# Wait for the specified lock duration
time.sleep(lock_duration)

# Unlock the system
os.system("killall xtrlock; killall feh")

# Remove the background image
os.system("xsetroot -solid black")  # Set background to black

# Notify the user that the system is unlocked
subprocess.Popen(["zenity", "--info", "--text", "System unlocked.", "--title", "Timer"])
