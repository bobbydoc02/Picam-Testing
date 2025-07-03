from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from time import sleep 
import os 
import cv2
from picamera2.encoders import H264Encoder


def capture_frames(recording_length, output_directory, foldername):
 camera = Picamera2()
 video_config = camera.create_video_configuration()
 camera.configure(video_config)
 encoder = H264Encoder(bitrate=10000000)
 filepath = os.path.join(output_directory, "placeholdervideo.h264") #output folder to be submitted as argument 
 
 camera.start_recording(encoder, filepath)
 sleep(recording_length) #don't like this, should be more a precise timing  
 camera.stop_recording()
	
    # Read the video from specified path
 cam = cv2.VideoCapture(filepath)
 folderpath = os.path.join(output_directory, foldername)
 print(folderpath)

 try:
    
     # creating a folder named data
     if not os.path.exists(folderpath):
         os.makedirs(folderpath)

 # if not created then raise error
 except OSError:
     print ('Error: Creating directory of data')

 # frame
 currentframe = 0

 while(True):
    
     # reading from frame
     ret,frame = cam.read()

     if ret:
         # if video is still left continue creating images
         name = str(folderpath)  + '/frame' + str(currentframe) + '.tiff'
         print ('Creating: ' + name)
 
         # writing the extracted images
         cv2.imwrite(name, frame)
 
         # increasing counter so that it will
         # show how many frames are created
         currentframe += 1
     else:
         break
 # Release all space and windows once done
 cam.release()
 cv2.destroyAllWindows()
 return 0 
 


output_directory = "/home/aaron/Pictures/Picamtesting" 

capture_frames(5, output_directory, "cameraframes")





