from operator import xor
import numpy as np

the_state = 5
inlet1 = 0
inlet2 = 1
bit_list = [0]*16

for shift in range(50):

    new_value = xor((the_state & 1<<inlet1)>>inlet1, (the_state & 1<<inlet2)>>inlet2)

    the_state >>= 1

    if new_value:
        appender = new_value<<15
        the_state |= appender
    else:
        appender = ~(new_value<<15)
        the_state &= appender

    for shift_amt in range(15, -1, -1):
        bit_value = (the_state & (1<<shift_amt))>>shift_amt
        bit_list[15-shift_amt] = bit_value

    print(bit_list)


class shift_register:

    def __init__(self, initial_state=None, length=3):
        if initial_state != None:
            self.state = np.array(initial_state)
            self.length = len(self.state)
        else:
            self.length = length
            self.state = np.zeros(self.length)

    def print_state(self):
         print(str(self.state) + " " + str(self.state))

    def shift(self):
        self.state = np.roll(self.state, 1)
        self.state[0] = 0

    def input(self, input_index, input_value):
        self.state[input_index] = input_value

    def XOR(self, tap1, tap2):
        return (int(self.state[self.length - 1 - tap1]) ^ int(self.state[self.length - 1 - tap2]))

sr1 = shift_register(length=18)
sr1.input(8, 1)
sr1.input(9, 1)
for iteration in range(10):
    for a_shift in range(sr1.length-1):
        sr1.shift()
        sr1.input(0, sr1.XOR(0, 1))
    sr1.print_state()
