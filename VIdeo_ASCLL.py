import cv2
import os
import time


ascii_chars = " `.,-':<>;+!*/?%&98#"
coef = 255 / (len(ascii_chars) - 1)


video_path = "Video/Bad_Apple.mp4"  


ascii_width = 120  
ascii_height = 40  

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("NO VIDEO FOUND")
    exit()

# FPS 
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    print("ERROR FPS")
    fps = 30  

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break 

        resized_frame = cv2.resize(frame, (ascii_width, ascii_height))

        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        ascii_art = ""
        for y in range(ascii_height):
            line = ""
            for x in range(ascii_width):
                brightness = gray_frame[y, x]
                char = ascii_chars[int(brightness / coef)]
                line += char
            ascii_art += line + "\n"

 
        os.system("cls" if os.name == "nt" else "clear") #Clear on OS
        print(ascii_art)


        time.sleep(1 / fps)

except KeyboardInterrupt:
    print("STOP")

finally:
    cap.release()
