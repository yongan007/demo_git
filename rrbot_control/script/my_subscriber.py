#!/usr/bin/env python
import rospy

from sensor_msgs.msg import JointState

def callback(data):


    joint_vale = data.position

    rospy.loginfo("joint post = "+ str(joint_vale))


def main():

   
    rospy.init_node('my_joint_angle', anonymous=True)

    rospy.Subscriber("/rrbot/joint_states", JointState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()