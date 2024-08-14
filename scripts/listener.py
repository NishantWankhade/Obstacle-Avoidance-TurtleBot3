#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

# Importing the LaserScan module
from sensor_msgs.msg import LaserScan

def admissible(range):
    if range > 1.5 or str(range) == "inf":
        print(str(range))
        return True
    else: return False 

def talker(pub, rate):
    while not rospy.is_shutdown():
        pub.publish(hello_str)
        rate.sleep()

def callback(data, args):
    at_front = data.ranges[0]

    publisher_node = args[0]
    sleep_rate = args[1]

    while(admissible(at_front)):
        talker(publisher_node, sleep_rate)

    ## TODO --> Logic for the code


def listener():
    rospy.init_node('listener', anonymous=True)

    rate = rospy.Rate(10) # 10hz
    publisher = rospy.Publisher('cmd_vel', String, queue_size=10)

    rospy.Subscriber('scan', LaserScan, callback, [publisher, rate])

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
