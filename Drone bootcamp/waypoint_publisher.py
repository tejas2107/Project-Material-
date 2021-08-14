import math
import numpy as np
import time
import rospy
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Transform, Quaternion
import std_msgs.msg
from geometry_msgs.msg import Point
import tf
rospy.init_node('waypoint_publisher', anonymous=True)
i=0
angular_velocity=(math.pi/12)
velocity_z=1.5
ardrone_command_publisher = rospy.Publisher('/ardrone/command/trajectory', MultiDOFJointTrajectory, queue_size=10)
while(i<=150):
    desired_yaw_to_go_degree=10*i

    desired_x_to_go=3*math.sin(angular_velocity*i)
    desired_y_to_go=3*math.cos(angular_velocity*i)
    desired_z_to_go=velocity_z*i

    quaternion = tf.transformations.quaternion_from_euler(0, 0, math.radians(desired_yaw_to_go_degree))

    traj = MultiDOFJointTrajectory()

    header = std_msgs.msg.Header()
    header.stamp = rospy.Time()
    header.frame_id = 'frame'
    traj.joint_names.append('base_link')
    traj.header=header

    transforms =Transform(translation=Point(desired_x_to_go, desired_y_to_go, desired_z_to_go), rotation=Quaternion(quaternion[0],quaternion[1],quaternion[2],quaternion[3]))

    velocities =Twist()
    accelerations=Twist()
    point = MultiDOFJointTrajectoryPoint([transforms],[velocities],[accelerations],rospy.Time(2))

    traj.points.append(point)

    time.sleep(1)
    ardrone_command_publisher.publish(traj)
    i=i+1
