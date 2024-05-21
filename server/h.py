import keyboard
import time


for i in range(50):
    time.sleep(0.5) 

    keyboard.write("@")

    time.sleep(0.7) 

    keyboard.write("52")

    keyboard.send("enter")
    keyboard.send("enter")