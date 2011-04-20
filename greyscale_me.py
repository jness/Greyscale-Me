#!/usr/bin/env python
import Image
import argparse

# Build my Parser with help for user input
parser = argparse.ArgumentParser()
parser.add_argument('message', help='Your message you wish to hide in a Grey Scale')
parser.add_argument('filename', help='This is the name of the image')
args = parser.parse_args()

# Get the chr() for each of your inputed characters
barcode_data = {}
count = 0
for letter in args.message:
    barcode_data[count] = ord(letter)
    count += 1

# Define Image properties
width = len(barcode_data) * 10
height = 20
size = (width, height)

# Create the new image object
im = Image.new('L', size) 

# just like a printer we will print a color code
# one pixel at a time
vcursor = 0
while vcursor < height:
    cursor = 0
    letter = 0
    while cursor < width:
        color = barcode_data[letter]
        for i in range(0, 10):
            position = (cursor, vcursor)
            im.putpixel(position, color)
            cursor += 1
        letter += 1
    vcursor += 1

# Image is created, lets save it to the file
im.save(args.filename)
