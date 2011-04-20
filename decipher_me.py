#!/usr/bin/env python
import Image
import argparse

# Build my Parser with help for user input
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='This is the name of the image')
args = parser.parse_args()

# Load our image
im = Image.open(args.filename)
width = im.size[0]

# Extract the color codes
string = ''
cursor = 0
while cursor < width:
    string = string + chr(im.getpixel((cursor, 0)))
    cursor += 10

# Print out the message
print string
