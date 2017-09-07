#!/usr/bin/env python

import roslib
import rospy

from visualization_msgs.msg import Marker


if __name__ == '__main__':

    rospy.loginfo('Starting Cube')
    base_frame = '/map'
    marker_topic = 'cube'

    # init node
    rospy.init_node('cube_node', anonymous=True)

    # make the cube object
    cube_marker = Marker()
    cube_marker.header.frame_id = base_frame
    cube_marker.id = 0
    cube_marker.ns = 'Cube'
    cube_marker.action = cube_marker.ADD
    cube_marker.type = cube_marker.CUBE
    cube_marker.lifetime = rospy.Duration(0.0)

    pub_cube = rospy.Publisher(marker_topic, Marker, queue_size=10)

    # wait while subscribers are detected on the publisher
    current_subscribers = pub_cube.get_num_connections()
    rospy.loginfo('Waiting for subscribers ...')
    while (current_subscribers == 0):
                rospy.Rate(100).sleep()
                current_subscribers = pub_cube.get_num_connections()

    # start sending the msg
    rospy.loginfo('Starting msg ...')

    while not rospy.is_shutdown():

        cube_marker.header.stamp = rospy.Time.now()

        # marker position
        cube_marker.pose.position.x = 0.0
        cube_marker.pose.position.y = 0.0
        cube_marker.pose.position.z = 0.0

        # marker pose
        cube_marker.pose.orientation.x = 0.0
        cube_marker.pose.orientation.y = 0.0
        cube_marker.pose.orientation.z = 0.0
        cube_marker.pose.orientation.w = 1.0

        # marker scale
        cube_marker.scale.x = 1.0
        cube_marker.scale.y = 1.0
        cube_marker.scale.z = 1.0

        # marker colors
        # a (alpha) must be non-zero
        cube_marker.color.a = 1.0
        cube_marker.color.r = 1.0
        cube_marker.color.g = 0.0
        cube_marker.color.b = 0.0

        # publish msg
        pub_cube.publish(cube_marker)
        rospy.Rate(10).sleep()

    rospy.loginfo('rospy shutdown')
