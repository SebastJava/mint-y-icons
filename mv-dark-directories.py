#!/usr/bin/python3
import os
import subprocess
import sys

colors = ["Aqua", "Blue", "BlueDeep", "Grey", "Mint", "MintContrast", "Orange", "Pink", "Purple", "PurpleDeep", "Red", "Yellow"]
path = "usr/share/icons"
os.system("cd %s" % path)

for color in colors:
    os.system("mv Mint-Yz-Mint-Dark Mint-Yz-%s-Dark" % color)

