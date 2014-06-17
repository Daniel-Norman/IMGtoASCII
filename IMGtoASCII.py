'''
Created on Jun 14, 2014

@author: Daniel Norman
'''

import Image
import sys
import urllib, cStringIO

reverseChars = False
chars = ' .-,=:^+<%I*LZAM#&@'

def getChar(color):
    index = (255 - color) / 255.0 * (len(chars) - 1)
    if reverseChars:
        index = len(chars) - 1 - index
    return chars[int(round(index))]

boxW = 2
boxH = 3

filename = raw_input("Enter an image file path: ")
if 'http' in filename:
    file_name = cStringIO.StringIO(urllib.urlopen(filename).read())
im = Image.open(file_name).convert('L')

size = float(raw_input("Enter a size (in chars): ")) * 2
if (raw_input("Reverse colors? (y/n): ") in 'yesYes'):
    reverseChars = True

width, height = im.size
scale = size / max(width, height)
width, height = int(round(width * scale)), int(round(height * scale))
im = im.resize((width, height))
    

for y in range(0, height, boxH):
    for x in range(0, width, boxW):
        image = im.crop((x, y, x + boxW, y + boxH))
        totalColor = 0
        for count, color in image.getcolors(boxW * boxH):
            totalColor += count * color
        sys.stdout.write(getChar(totalColor / (boxW * boxH)))
    print '\n',
    
sys.stdout.flush()
