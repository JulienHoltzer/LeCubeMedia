import cv2
import logging
import thread

def video_capture(cube,idcam):
    capture = cv2.videoCapture(idcam)
    while True:
        ret, frame = self.capture.read()
        cube.video_frame(idcam,frame)

    
def init(pub, cube, params):
    idcam = params.get('idcam',0)
    logging.info("Launching video capture thread for video device #%s"%idcam)
    thread.start_new_thread(video_capture, (cube,idcam))
