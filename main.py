# main deps
import pyautogui
import autoit
import keyboard

# util deps
import yaml
import random
import decimal
import time
import threading

# globals
config=None
detectShake=False

# so we can reload the config whenever we want
def readConfig():
    global config
    with open('./config.yaml') as f:
        config = yaml.safe_load(f)
        print("config loaded!")

readConfig()

def on():
    while True:
        if detectShake:
            try:
                screen = config['screen']
                location = pyautogui.locateOnScreen(config['button_img'], region=(0,0,screen['w'],screen['h']), confidence=0.7)
                if location != None:
                    location = pyautogui.center(location)
                    x, y = location
                    autoit.mouse_click('left', x, y)
                    print("found!!!!!")
            except:
                pass
        
            time.sleep(float(random.randrange(4,7)/10))
        else:
            time.sleep(0.05)

t = threading.Thread(target=on)
t.daemon = True
t.start()
while True:
    if keyboard.read_key() == config['keybinds']['toggle']:
        detectShake ^= True
        print("running: " + str(detectShake))
        time.sleep(0.2)

    elif keyboard.read_key() == config['keybinds']['exit']:
        exit()

    elif keyboard.read_key() == config['keybinds']['reload_config']:
        readConfig()

