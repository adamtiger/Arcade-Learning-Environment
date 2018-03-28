import gym
import numpy as np
import csv
import time

env = gym.make('GoalbasedMsPacman-ram-v0')
env.setup((65, 98, 75, 98))
env.reset()

"""
exit = False
for i in range(100):
    ram_0, _, done, _ = env.step(0)

while not exit:
    step = input() # numbers 0-8
    
    ram, _, done, _ = env.step(int(step))
    if done:
        env.reset()
    print(ram.astype(int) - ram_0.astype(int))
    print(ram)
    ram_0 = ram
    with open('periodic.csv', 'a', newline='') as f:
        wrt = csv.writer(f, delimiter=',')
        wrt.writerow(ram.tolist())
    env.render()
    exit = int(step) == 10
"""

eps = 0
while eps < 10:
    _, rw, done, _ = env.step(env.action_space.sample())
    env.render()
    time.sleep(0.05)
    if done:
        env.reset()
        if rw:
            print("--- Termination --- Victory")
        else:
            print("--- Termination ---")
        eps += 1
