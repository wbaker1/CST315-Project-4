#CST-305 Project 4 - Matthew Powers and Wesley Baker 
#This project is a display of the equtions solved for project 4

import numpy as np
import matplotlib.pyplot as plt

def part_2_result_1(t):
    return np.exp(-t/20)

def part_2_result_2(t):
    return -1*np.exp(-t/20)

#################################################################
# plot results for part 2
# time points
t = np.linspace(-100,100,1000)
plt.plot(t,part_2_result_1(t),'b-', label='Part 2 first X(t) line')

plt.plot(t,part_2_result_2(t),'r-', label='Part 2 second X(t) line')

# label neccessary info on graph
plt.title('Part 2')
plt.xlabel('t val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################
