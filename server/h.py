import keyboard
import time

time.sleep(1)

for i in range(50):
    # time.sleep(0.5) 

    keyboard.write("/stat@combot")


    keyboard.send("enter")