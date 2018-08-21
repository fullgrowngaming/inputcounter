#I know this is super hacky and doesn't count inputs yet AND doesn't handle multiple buttons at the same time AND
#never breaks out of the loop, but I'm proud to have gotten this far fggYay

from websocket import *

ws = create_connection("ws://nintendowispy.local:18881")
print("Receiving...")
while 1:
    data = ws.recv()
    b = str(bytes(data, 'utf-8'))
    c = b.strip("b'")
    d = list(c)
    if len(d) == 9:
        pass
    elif len(d) != 9:
        if d[15] == '1':
            print('Start')
        elif d[19] == '1':
            print('Y')
        elif d[23] == '1':
            print('X')
        elif d[27] == '1':
            print('B')
        elif d[31] == '1':
            print('A')
        elif d[39] == '1':
            print('L')
        elif d[43] == '1':
            print('R')
        elif d[47] == '1':
            print('Z')
        elif d[51] == '1':
            print('D-Up')
        elif d[55] == '1':
            print('D-Down')
        elif d[59] == '1':
            print('D-Right')
        elif d[63] == '1':
            print('D-Left')

ws.close()
