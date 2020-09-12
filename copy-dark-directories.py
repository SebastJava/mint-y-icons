#!/usr/bin/python3
import os
import subprocess
import sys

colors = ["Aqua", "Blue", "BlueDeep", "Grey", "MintContrast", "Orange", "Pink", "Purple", "PurpleDeep", "Red", "Yellow"]

os.chdir("usr/share/icons/")

for color in colors:
    os.system("cp -r Mint-Yz-Mint-Dark Mint-Yz-%s-Dark" % color)

