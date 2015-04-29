#!/usr/bin/python
from sys import argv
import zbar
import cv2
import Image

def scanImage(scanner,image):
    scanner.scan(image)
    # extract results
    for symbol in image:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data


if len(argv) < 2: exit(1)

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
#imraw = cv2.imread(argv[1],cv2.CV_LOAD_IMAGE_COLOR)
#img = cv2.cvtColor(imraw, cv2.COLOR_BGR2GRAY)

fname = argv[1]

#Open image with openCV
cvimg = cv2.imread(fname,cv2.CV_LOAD_IMAGE_GRAYSCALE)
cvheight, cvwidth = cvimg.shape
cvraw = cvimg.tostring()

#Open image with PIL
pilimg = Image.open(fname).convert('L')
pilwidth, pilheight = pilimg.size
pilraw = pilimg.tostring()

# wrap image data
#image = zbar.Image(width, height, 'Y800', img.tostring())
cvzbimg  = zbar.Image(cvwidth, cvheight, 'GREY', cvraw)
pilzbimg = zbar.Image(pilwidth, pilheight, 'GREY', pilraw)

# scan the image for barcodes
print "-----"
print "Scanning image opened with opencv :"
print cvwidth, cvheight
scanImage(scanner,cvzbimg)
print "-----"
print "Scanning image opened with PIL :"
print pilwidth, pilheight
scanImage(scanner,pilzbimg)
print "-----"

    
#cv2.imshow("a",img)
#cv2.waitKey(0)
# clean up
#del(image)
