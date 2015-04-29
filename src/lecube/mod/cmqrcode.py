import zbar
import cv2
import logging


class BarCodeFinder :

    Instance = None

    def __init__(self, pub, cube):
        self.pub = pub
        self.cube = cube
        self.scanner = zbar.ImageScanner()
        self.scanner.parse_config('enable')
        self.symbols = []

    def qr_decode(self,idcam,frame):

            # Transform image, get useful info
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            h,w = gray.shape
            raw = gray.tostring()

            # Find symbols in the image
            img = zbar.Image(w,h,'GREY',raw)
            scanner.scan(img)

            # Call event for newly detected symbols
            cursym = []
            for rawsymbol in img:
                tag = (symbol.type, symbol.data)
                cursym.add(tag)
                if not symbol in self.symbols:
                    cube.tag_detection(tag)

            # Store current symbols
            self.symbols = cursym

def init(pub, cube, params):
    logging.info("Subscribing barcode decoder to live frame captures")
    BarCodeFinder.Instance = BarCodeFinder(pub,cube,device)
    pub.subscribe(BarCodeFinder.Instance.qr_decode,'new-live-video-frame')
    
