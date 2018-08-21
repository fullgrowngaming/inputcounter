#http://nintendowispy.keepdream.in/?theme=Kylf&websockport=18881&websocketserver=NintendoWiSpy.local&inputdelay=275

from websocket import *

ws = create_connection("ws://nintendowispy.local:18881")
print("Receiving...")
while 1:
    data = ws.recv()
    b = str(bytes(data, 'utf-8'))
    c = b.strip("b'")
    d = list(c)
    buttons = []
    if len(d) == 9:
        pass
    elif len(d) != 9:
        buttons = {'Start': d[15], 'Y': d[19], 'X': d[23], 'B': d[27], 'A': d[31], 'L': d[39], 'R': d[43], 'Z': d[47],
                   'D-Up': d[51], 'D-Down': d[55], 'D-Right': d[59], 'D-Left': d[63]}

    for button in buttons:
        if buttons[button] == '1':
            print(button)

ws.close()
