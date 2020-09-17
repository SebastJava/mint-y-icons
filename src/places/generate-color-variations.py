#!/usr/bin/python3
import os

# This script uses green.svg and generates the other COLOR.svg files from it.
# It uses the following color table to do so:
COLORS = {}
COLORS["Mint"] = "0AC266"
COLORS["MintContrast"] = "18AA60"
COLORS["Grey"] = "767676"
COLORS["Red"] = "FF192D"
COLORS["Orange"] = "FF741A"
COLORS["Aqua"] = "00AACC"
COLORS["Blue"] = "1A80E5"
COLORS["BlueDeep"] = "3653E2"
COLORS["PurpleDeep"] = "731DC8"
COLORS["Purple"] = "A528CD"
COLORS["Pink"] = "FF3376"
COLORS["Yellow"] = "FFCC33"

GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
