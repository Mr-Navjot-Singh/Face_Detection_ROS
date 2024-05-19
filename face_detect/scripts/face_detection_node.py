#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def face_detection():
    rospy.init_node('face_detection_node', anonymous=True)
    rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)
    rospy.spin()

def image_callback(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(cv_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Face Detection', cv_image)
    cv2.waitKey(1)

if __name__ == '__main__':
    try:
        face_detection()
    except rospy.ROSInterruptException:
        pass
