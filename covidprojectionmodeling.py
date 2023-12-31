# -*- coding: utf-8 -*-
"""CovidProjectionModeling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12y-E0gMzgau_14WFqvA_imMQh-IWyYcd
"""

import matplotlib.pyplot as plt
import numpy as np

S_list = []
R_list = []
I_list = []

# parameters:
# b is infection rate
b = 0.0608
# g is recovery rate
g = 0.0376
# m is loss of immunity rate
m = 0.082
# vr is vaccination rate
vr = .5
# ve is vaccine efficacy
ve = .7
v = 1 - vr * ve
deltat = 1
# N in population
N = 6.15e6

# Variables/Initial Values:
S = 1
I = 1388 / N
R = 0

t0 = 0
tf = 1500
n = (tf - t0) / deltat

# Euler's method:
for j in range(int(n)):
    S = S - ((v * b * S * I) + m * R) * deltat
    I = I + ((v * b * S * I) - (g * I)) * deltat
    R = R + (g * I - m * R) * deltat
    S_list.extend([S * N])
    I_list.extend([I * N])
    R_list.extend([R * N])

# t = np.array([range(int(n))])
# S_plot = np.array(S_list)
# plt.scatter(t, S_plot, label="Susceptible", color="blue", s=20)

t = np.array([range(int(n))])
I_plot = np.array(I_list)
plt.scatter(t, I_plot, label="Infected", color="red", s=4)

t = np.array([range(int(n))])
R_plot = np.array(R_list)
plt.scatter(t, R_plot, label="Recovered", color="green", s=4)

# x-axis label
plt.xlabel('Time')
# frequency label
plt.ylabel('Number of Individuals')
# plot title
plt.title('Covid')

plt.legend()

print(I_list[300])
print(R_list[300])

# function to show the plot
plt.show()

quit()