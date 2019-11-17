#!/usr/bin/env python
import rospy

from mobile_base_driver.msg import ChestLeds
from mobile_base_driver.msg import Led


def lights():
	pub = rospy.Publisher('/denise/mobile_base/commands/chest_leds', ChestLeds, queue_size=10)
	rospy.init_node('lights', anonymous=False)
	light = ChestLeds()
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		for i in range(len(light.leds)):
			light.leds[i].red = 255
			light.leds[i].green = 0
			light.leds[i].blue = 0
		rospy.loginfo(light)
		pub.publish(light)
		rate.sleep()


if __name__ == '__main__':
	try:
		lights()
	except rospy.ROSInterruptException:
		pass