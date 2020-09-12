#!/usr/bin/python3
import os

# This script uses green.svg and generates the other COLOR.svg files from it.
# It uses the following color table to do so:
COLORS = {}
COLORS["Mint"] = "0AC266"
COLORS["MintContrast"] = "18AA60"
COLORS["Grey"] = "767676"
COLORS["Red"] = "E61A2C"
COLORS["Orange"] = "F46A25"
COLORS["Aqua"] = "00A2C2"
COLORS["Blue"] = "1E77D2"
COLORS["BlueDeep"] = "2A47D5"
COLORS["PurpleDeep"] = "731DC8"
COLORS["Purple"] = "AB2AD5"
COLORS["Pink"] = "E8316E"
COLORS["Yellow"] = "FFCC33"

GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
