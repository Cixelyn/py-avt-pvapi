"""Quick example demonstrating the functionality of avt-pvapi.py"""

from avt-pvapi.py import *


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

    sleep(3)
    frame = c.captureFrame(cam)
    sleep(3)


    print c.commandRun(cam,"AcquisitionStop")
    print c.captureEnd(cam)
    
    
    print c.cameraClose(cam)
    
    

    print c.attrUint32Get(cam,"StatFramesCompleted")    
    
    
    c.uninitialize()
    
    imbuff = frame.ImageBuffer
    converted = [ord(imbuff[x]) for x in range(322752)]
    resized = array(converted).reshape(492,656)
    pylab.imshow(resized)


