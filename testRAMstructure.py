import sys
from random import randrange
from ale_python_interface import ALEInterface
import numpy as np
import matplotlib.pyplot as plt

ale = ALEInterface()

# Get & Set the desired settings
ale.setInt(b'random_seed', 123)

# Set USE_SDL to true to display the screen. ALE must be compilied
# with SDL enabled for this to work. On OSX, pygame init is used to
# proxy-call SDL_main.
USE_SDL = False
if USE_SDL:
  if sys.platform == 'darwin':
    import pygame
    pygame.init()
    ale.setBool('sound', False) # Sound doesn't work on OSX
  elif sys.platform.startswith('linux'):
    ale.setBool('sound', True)
  ale.setBool('display_screen', True)

# Load the ROM file
rom_file = str.encode('ms_pacman.bin')
ale.loadROM(rom_file)

# Get the list of legal actions
legal_actions = ale.getLegalActionSet()
"""
# Play 10 episodes
num = 10
cntr = 0
rams_mv = []
while cntr < num:
  cntr += 1
  a = legal_actions[randrange(len(legal_actions))]
  # Apply an action and get the resulting reward
  reward = ale.act(2)
  rams_mv.append(ale.getRAM())
  if ale.game_over():
    ale.reset_game()

cntr = 0
rams_0 = []
while cntr < num:
  cntr += 1
  # Apply an action and get the resulting reward
  reward = ale.act(0)
  rams_0.append(ale.getRAM())
  if ale.game_over():
    ale.reset_game()
"""
# Finding the rest parts of the RAM
"""
mv = np.ndarray(rams_mv[0].shape, dtype=bool)
mv[:] = True
temp = rams_mv[0]
for ram in rams_mv:
  mv = np.equal(mv, (np.equal(temp, ram)))
  temp = ram

st = np.ndarray(rams_0[0].shape, dtype=bool)
st[:] = True
temp = rams_0[0]
for ram in rams_0:
  st = np.equal(st, (np.equal(temp, ram)))
  temp = ram

diff = np.equal(mv, st)
print(diff)
for idx in range(0, diff.shape[0]):
  if not diff[idx]:
    print (idx)
"""

ale.reset_game()
ram = ale.getRAM()
ram[16] = 98
ram[10] = 66
ale.alterEmulatorRAM(ram)
ale.act(1)
plt.imshow(ale.getScreenRGB())
plt.show()
for i in range(800):
    ale.act(2)
plt.imshow(ale.getScreenRGB())
plt.show()
for i in range(20):
   plt.imshow(ale.getScreenRGB())
   plt.show()
   ale.act(4)
   print(ale.getRAM())



