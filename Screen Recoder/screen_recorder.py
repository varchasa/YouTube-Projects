
import sys
import time
import numpy

from screen_recorder_sdk import screen_recorder

def main ():
    hours = int(input("enter : "))
    seconds = int(input("enter : "))
    screen_recorder.enable_dev_log ()
    
    params = screen_recorder.RecorderParams ()
    # params.pid = 0 # use it to set process Id to capture
    # params.desktop_num = 0 # use it to set desktop num, counting from 0
     #intialize the screen recoder
    screen_recorder.init_resources (params)
    #take screenshot and save it 
    screen_recorder.get_screenshot (5).save ('test_before.png')
    #start video recording
    screen_recorder.start_video_recording ('video1.mp4', 30, 8000000, True)
    #time limit 
    time.sleep (hours*60+seconds)
    
    
    #stp the recording
    screen_recorder.stop_video_recording ()


if __name__ == "__main__":
    main ()
