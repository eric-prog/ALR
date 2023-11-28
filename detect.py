import RPi.GPIO as GPIO
from time import sleep
import sys

import numpy as np
import cv2

motor_channel = (29,31,33,35)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(motor_channel, GPIO.OUT)

motor_direction = input('select motor direction a=anticlockwise, c=clockwise: ')

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
	try:
		ret, img = cap.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(
			gray,     
			scaleFactor=1.2,
			minNeighbors=5,     
			minSize=(20, 20)
		)
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]  
		cv2.imshow('video',img)
		k = cv2.waitKey(30) & 0xff
    
		if (motor_direction == 'c'):
			print('motor running clockwise \n')
			GPIO.output(motor_channel, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
			sleep(0.002)
			GPIO.output(motor_channel, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
			sleep(0.002)
			GPIO.output(motor_channel, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
			sleep(0.002)
			GPIO.output(motor_channel, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
			sleep(0.002)
		elif(motor_direction == 'a'):
			print('motor running anti-clockwise \n')
			GPIO.output(motor_channel, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
			sleep(0.002)
			GPIO.output(motor_channel, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
			sleep(0.002)
			GPIO.output(motor_channel, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
			sleep(0.002)
			GPIO.output(motor_channel, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
			sleep(0.002)
		
	except KeyboardInterrupt:
		motor_direction = input('select motor direction a=anticlockwise, c=clockwise or q=exit ')
		if(motor_direction == 'q' or  k == 27):
			print('motor stopped')
			sys.exit(0)
			break;
			
cap.release()
cv2.destroyAllWindows()



# import numpy as np
# import cv2
# import serial

# import RPi.GPIO as GPIO
# from time import sleep
# import sys

# motor_channel = (29,31,33,35)
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(motor_channel, GPIO.OUT)

# # #sets how many pixels away from the center a person needs to be before the head stops
# center_tolerance = 15;

# # initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# cv2.startWindowThread()

# # open webcam video stream
# cap = cv2.VideoCapture(0)

# while(True):
    # ret, frame = cap.read()# Capture frame-by-frame
    # frame = cv2.resize(frame, (150, 150))# resizing for faster detection
    # boxes, weights = hog.detectMultiScale(frame, winStride=(1,1), scale = 1.05)# detect people in the image
    # boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])# returns the bounding boxes for the detected objects
    # centers = []

    # for box in boxes:#get the distance from the center of each box's center x cord to the center of the screen and ad them to a list
        # center_x = ((box[2]-box[0])/2)+box[0]
        # x_pos_rel_center = (center_x-70)
        # dist_to_center_x = abs(x_pos_rel_center)
        # centers.append({'box': box, 'x_pos_rel_center': x_pos_rel_center, 'dist_to_center_x':dist_to_center_x})    
    
    # if len(centers) > 0:
        # sorted_boxes = sorted(centers, key=lambda i: i['dist_to_center_x'])#sorts the list by distance_to_center
        # center_box = sorted_boxes[0]['box']#draws the box

        # for box in range(len(sorted_boxes)):
        # # display the detected boxes in the colour picture
            # if box == 0:
                # cv2.rectangle(frame, (sorted_boxes[box]['box'][0],sorted_boxes[box]['box'][1]), (sorted_boxes[box]['box'][2],sorted_boxes[box]['box'][3]), (0,255, 0), 2)
            # else:
                # cv2.rectangle(frame, (sorted_boxes[box]['box'][0],sorted_boxes[box]['box'][1]), (sorted_boxes[box]['box'][2],sorted_boxes[box]['box'][3]),(0,0,255),2)
        # #retrieves the distance from center from the list and determins if the head should turn left, right, or stay put.
        # Center_box_pos_x = sorted_boxes[0]['x_pos_rel_center']  
        
        # if -center_tolerance <= Center_box_pos_x <= center_tolerance:
            # # remain stationary
            # print("center")

        # elif Center_box_pos_x >= center_tolerance:
            # #turn head to the right
            # print("right")
            # GPIO.output('c', (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
            # sleep(0.002)
            # GPIO.output('c', (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
            # sleep(0.002)
            # GPIO.output('c', (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
            # sleep(0.002)
            # GPIO.output('c', (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
            # sleep(0.002)
        # elif Center_box_pos_x <= -center_tolerance:
            # #turn head to the left
            # GPIO.output('a', (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
            # sleep(0.002)
            # GPIO.output('a', (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
            # sleep(0.002)
            # GPIO.output('a', (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
            # sleep(0.002)
            # GPIO.output('a', (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
            # sleep(0.002)
        # print(str(Center_box_pos_x))
    # else:
        # #prints out that no person has been detected
        # print("nothing detected")
    # #resizes the video so its easier to see on the screen
    # frame = cv2.resize(frame,(720,720))
    # # Display the resulting frame
    # cv2.imshow("frame",frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break


    
# cap.release()# When everything done, release the capture
# cv2.destroyAllWindows()# close the window
# cv2.waitKey(1)


