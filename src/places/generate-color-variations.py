#!/usr/bin/python3
import os

# This script uses green.svg and generates the other COLOR.svg files from it.
# It uses the following color table to do so:
COLORS = {}
COLORS["MintSoda"] = "29BF69"
COLORS["MintLeaf"] = "00B894"
COLORS["BlueBelize"] = "2980B9"
COLORS["BlueElectron"] = "0984E3"
COLORS["Purple"] = "9547B6"
COLORS["Pink"] = "F655A5"
COLORS["Grey"] = "6C7879"
COLORS["RedShine"] = "F92031"
COLORS["OrangeShine"] = "FF780A"
COLORS["AquaShine"] = "00ACE5"
COLORS["Yellow"] = "F5C73D"

GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
