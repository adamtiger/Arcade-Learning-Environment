import gym
import numpy as np
import csv

env = gym.make('MsPacman-ram-v0')
env.reset()

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
