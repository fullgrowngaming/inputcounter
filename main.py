#sloppy, perhaps, but this is the first version of my program that actually works!

from websocket import *
import sys

connected = False

while not connected:
    try:
        ws = create_connection("ws://nintendowispy.local:18881")
        connected = True
    except:
        print("Could not connect, retrying...")

print("Receiving...")

press_counter = {'Start': 0, 'Y': 0, 'X': 0, 'B': 0, 'A': 0, 'L': 0, 'R': 0, 'Z': 0, 'D-Up': 0, 'D-Down': 0,
                        'D-Right': 0, 'D-Left': 0}

previous_buttons = []

while 1:

    data = ws.recv()
    b = str(bytes(data, 'utf-8'))
    c = b.strip("b'")
    d = list(c)

    if len(d) == 9:
        pass
    elif len(d) != 9:
        buttons = {'Start': d[15], 'Y': d[19], 'X': d[23], 'B': d[27], 'A': d[31], 'L': d[39], 'R': d[43], 'Z': d[47],
                   'D-Up': d[51], 'D-Down': d[55], 'D-Right': d[59], 'D-Left': d[63]}

        for button in buttons:
            if buttons[button] == '1':
                if button not in previous_buttons:
                    previous_buttons.append(button)
                    press_counter[button] += 1
                    print(press_counter)
            else:
                try:
                    previous_buttons.remove(button)
                except:
                    pass

ws.close()
