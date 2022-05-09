#!/usr/bin/env python



import rospy
# from std_msgs.msg import String

from sensor_msgs.msg import JointState 

def callback(msg):


    joint1_pose = msg.position

    rospy.loginfo("joint post = "+ str(joint1_pose))

    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def main():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('robot_joint_angle', anonymous=True)

    rospy.Subscriber("/rrbot/joint_states", JointState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()