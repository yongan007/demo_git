#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def publisher():
    
    rospy.init_node('publisher', anonymous=True)

    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    
    rate = rospy.Rate(50) # 10hz
    while not rospy.is_shutdown():
     
        position = -math.pi/6
        # position1 = math.pi/6
        # position2 = -math.pi/12

        rospy.loginfo(position)
        
        pub1.publish(-math.pi/6)
        pub2.publish(math.pi/6)
    
        rate.sleep()

    # return position

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass