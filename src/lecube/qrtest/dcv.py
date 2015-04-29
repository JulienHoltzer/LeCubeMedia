#!/usr/bin/python
from sys import argv
import zbar
import cv2

if len(argv) < 2: exit(1)

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
#imraw = cv2.imread(argv[1],cv2.CV_LOAD_IMAGE_COLOR)
#img = cv2.cvtColor(imraw, cv2.COLOR_BGR2GRAY)

img = cv2.imread(argv[1],cv2.CV_LOAD_IMAGE_GRAYSCALE)

width, height = img.shape

# wrap image data
#image = zbar.Image(width, height, 'Y800', img.tostring())
image = zbar.Image(width, height, 'GREY', img.tostring())

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
    
#cv2.imshow("a",img)
#cv2.waitKey(0)
# clean up
#del(image)
