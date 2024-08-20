#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import math

# Importing the LaserScan module
from sensor_msgs.msg import LaserScan

# Importing the datatype required for publishing to the CMD_VEL topic
from geometry_msgs.msg import Twist

# TurtleBot --> Burger's Dimensions
WIDTH = 178
RADIUS = 105

def admissible(range):
    ## TODO --> Logic for the code

    # Check objects in Vicinity
    angle = int(math.degrees(math.asin((1.0 * WIDTH/2) / RADIUS)))
    range_list = range[-angle:] + range[0:angle]

    for i in range_list:
        if i != "inf" and i < 0.2: return False
    return True 

def talker(pub, range):
    vel = Twist()
    if admissible(range) == True: 
        vel.linear.x = 0.15
        vel.angular.z = 0
    else:
        vel.angular.z = 0.2
        vel.linear.x = 0
    pub.publish(vel)

def callback(data, args):
    range = data.ranges
    publisher_node = args[0]
    talker(publisher_node, range)

def listener():
    rospy.init_node('listener', anonymous=True)

    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    rospy.Subscriber('scan', LaserScan, callback, [publisher])

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
