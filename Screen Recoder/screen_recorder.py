import sys
import time

from screen_recorder_sdk import screen_recorder 

def main ():
    
    hours = int(input("Hours : "))
    seconds = int(input("Seconds : "))
    
    #enable dev logger
    screen_recorder.enable_dev_log ()
    
    params = screen_recorder.RecorderParams ()
   
    #intialize the screen recoder
    screen_recorder.init_resources (params)
    
    #take screenshot and save it 
    screen_recorder.get_screenshot (5).save ('sample.png')
    print('Screenshot taken')
    
    #start video recording
    print('Video Started')
    screen_recorder.start_video_recording ('sample.mp4', 30, 8000000, True)
    
    #time limit 
    time.sleep (hours*60+seconds)
    
    #stop the recording
    screen_recorder.stop_video_recording ()
    print('Video Stopped')


if __name__ == "__main__":
    main ()
