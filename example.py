"""Quick example demonstrating the functionality of avt-pvapi.py"""


import numpy as np
from pvapi import *
import matplotlib.pyplot as plt


if __name__=="__main__":
    
    c = CameraDriver()
    print c.initialize()
    
    uid = c.cameraList()[0].UniqueId
    print uid

    cam = c.cameraOpen(uid)

    print c.captureStart(cam)
    

    #print c.attrEnumSet(cam,"AcquisitionMode","Continuous")
    print c.attrEnumSet(cam,"FrameStartTriggerMode","Freerun")
    sleep(1)
    print c.commandRun(cam,"AcquisitionStart")    

    sleep(1)
    frame = c.captureFrame(cam)
    sleep(1)


    print c.commandRun(cam,"AcquisitionStop")
    print c.captureEnd(cam)
    
    
    print c.cameraClose(cam)
    
    

    print c.attrUint32Get(cam,"StatFramesCompleted")    
    
    
    c.uninitialize()
    
    imbuff = frame.ImageBuffer
    converted = [ord(imbuff[x]) for x in range(322752)]
    resized = np.array(converted).reshape(492,656)
    plt.imshow(resized)
    plt.show()


