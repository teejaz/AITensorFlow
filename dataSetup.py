import numpy as np
import matplotlib.pyplot as plt
import utils
import os
import urllib.request
import ssl


plt.style.use('ggplot')
files = os.listdir("C:/Users/tejas/Desktop/ART PROJECTS/animeface-character-dataset/animeface-character-dataset/thumb")

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

for dirname, dirnames, filenames in os.walk('C:/Users/tejas/Desktop/ART PROJECTS/animeface-character-dataset/animeface-character-dataset/thumb'):
    # print path to all subdirectories firste.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))
        # don't go into any .git directories.
    filenames = [file_i for file_i in filenames if '.png' in file_i]

print(filenames)

