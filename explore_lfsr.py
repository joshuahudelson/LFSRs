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


import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.xlim(-4.1, 4.1)
plt.plot(X, C, color="purple", linewidth=2.0, linestyle=":")
plt.plot(X, S, color="magenta", linewidth=0.5, linestyle=":")


"""
# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plot sine using green color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Set x limits
plt.xlim(-4.0,4.0)

# Set x ticks
plt.xticks(np.linspace(-4,4,9,endpoint=True))

# Set y limits
plt.ylim(-1.0,1.0)

# Set y ticks
plt.yticks(np.linspace(-1,1,5,endpoint=True))

# Save figure using 72 dots per inch
# savefig("../figures/exercice_2.png",dpi=72)

# Show result on screen
plt.show()
"""
plt.show()
