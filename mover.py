#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
def mover():
	publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	rospy.init_node('mover', anonymous=False)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		linear = Vector3(x=10.0, y=10.0, z=10.0)
		angular = Vector3(x=0.0, y=0.0, z=0.0)
		move_forward = Twist(linear, angular)
		rospy.loginfo(move_forward)
		publisher.publish(move_forward)
		rate.sleep()

if __name__ == '__main__':
	try:
		mover()
	except rospy.ROSInterruptException:
		pass
