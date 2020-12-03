#!/usr/bin/python3
import os

# This script uses green.svg and generates the other COLOR.svg files from it.
# It uses the following color table to do so:
COLORS = {}
COLORS["MintSoda"] = "40BF40"
COLORS["MintSoft"] = "14B866"
COLORS["Grey"] = "767676"
COLORS["Red"] = "FF1428"
COLORS["Orange"] = "FF7200"
COLORS["Aqua"] = "00AACC"
COLORS["Blue"] = "1A80E5"
COLORS["BlueDeep"] = "3753E2"
COLORS["PurpleDeep"] = "8033CC"
COLORS["Purple"] = "AA40BF"
COLORS["Pink"] = "FF4DA6"
COLORS["Yellow"] = "FFCC33"

GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
