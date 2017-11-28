from operator import xor
import numpy as np
import matplotlib.pyplot as plt
import copy

the_state = 5
inlet1 = 0
inlet2 = 1
bit_list = [0]*16

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

register_length = 20
num_loops = 30
num_subplots = register_length * num_loops
sr1 = shift_register(length=register_length)
sr1.input(10, 1)
plt.figure(1)
for loop in range(num_loops):
    plt.subplot(num_loops, 2, (loop * 2)+1)
    x = copy.deepcopy(sr1.state)
    plt.plot((np.concatenate((x, x))))
    plt.subplot(num_loops, 2, (loop*2)+2)
    plt.plot(np.fft.fft(x))
    for a_shift in range(sr1.length-1):
        sr1.shift()
        sr1.input(0, sr1.XOR(0, 1))


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
