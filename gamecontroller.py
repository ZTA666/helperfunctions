#this parses most infos from gamecontroller found in the lab
import hid
import time
from tqdm import tqdm
import numpy as np

class Controller():
    def __init__(self):
        self.cross = False
        self.square = False
        self.circle = False
        self.triangle = False

        self.up = False
        self.left = False
        self.right = False
        self.down = False

        self.joyLUD = 0
        self.joyLLR = 0
        self.joyRUD = 0
        self.joyRLR = 0

        self.L1 = False
        self.L2 = False

        self.L1 = False
        self.L2 = False

        self.gamepad = hid.device()
        self.gamepad.open(0x054c,0x05c4)
        self.gamepad.set_nonblocking(True)

        self.response = [1, 128, 128, 128, 128, 8, 0, 0, 0, 0]

    def close(self):
        self.gamepad.close(0x054c,0x05c4)

    def readRaw(self):
        self.response = self.gamepad.read(10)

    def resetButtons(self):
        self.cross = False
        self.square = False
        self.circle = False
        self.triangle = False

        self.up = False
        self.left = False
        self.right = False
        self.down = False

        self.joyLUD = 0
        self.joyLLR = 0
        self.joyRUD = 0
        self.joyRLR = 0

        self.L1 = False
        self.L2 = False

        self.R1 = False
        self.R2 = False

        self.share = False
        self.option = False

    def parse(self):
        #do the buttons
        self.resetButtons()
        self.readRaw()

        r = self.response
        if r:
            if r[5] == 40:
                self.cross = True
            if r[5] == 24:
                self.square = True
            if r[5] == 72:
                self.circle = True
            if r[5] == 136:
                self.triangle = True
            if r[5] == 0:
                self.up = True
            if r[5] == 2:
                self.left = True
            if r[5] == 4:
                self.down = True
            if r[5] == 6:
                self.right = True
            self.joyLLR = (r[1]-128)/256*2
            self.joyLUD = -(r[2]-128)/256*2
            self.joyRLR = (r[3]-128)/256*2
            self.joyRUD = -(r[4]-128)/256*2
            if r[6] == 2:
                self.R1 = True
            if r[6] == 8:
                self.R2 = True
            if r[6] == 1:
                self.L1 = True
            if r[6] == 4:
                self.L2 = True
            if r[6] == 16:
                self.share = True
            if r[6] == 32:
                self.option = True


    def get(self):
        self.parse()
        ret = {'buttons':[],'joy':dict(left=dict(lr=0,ud=0),right=dict(lr=0,ud=0))}
        if self.cross:
            ret['buttons'].append('cross')
        if self.square:
            ret['buttons'].append('square')
        if self.circle:
            ret['buttons'].append('circle')
        if self.triangle:
            ret['buttons'].append('triangle')
        if self.up:
            ret['buttons'].append('up')
        if self.left:
            ret['buttons'].append('left')
        if self.right:
            ret['buttons'].append('right')
        if self.down:
            ret['buttons'].append('down')
        if self.joyLUD != 0:
            ret['joy']['left']['ud'] = self.joyLUD
        if self.joyLLR != 0:
            ret['joy']['left']['lr'] = self.joyLLR
        if self.joyRUD != 0:
            ret['joy']['left']['ud'] = self.joyRUD
        if self.joyRLR != 0:
            ret['joy']['left']['lr'] = self.joyRLR
        if self.L1:
            ret['buttons'].append('l1')
        if self.L2:
            ret['buttons'].append('l2')
        if self.R1:
            ret['buttons'].append('r1')
        if self.R2:
            ret['buttons'].append('r2')
        if self.share:
            ret['buttons'].append('share')
        if self.option:
            ret['buttons'].append('option')
        return ret

c = Controller()
for i in range(10000):
    q = c.get()
    print(q)
    time.sleep(0.01)


#Hallo, das war Leah!

#Hallo, das war Leah!2.01

#comment from Tianao


