#!/usr/bin/env python3
from __future__ import print_function
from six.moves import input
import time
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from indy_utils import indydcp_client as client
from indy_utils.indy_program_maker import JsonProgramComponent
try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi

    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
def all_close(goal, actual, tolerance):

    if type(goal) is list:
        for index in range(len(goal)):
            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
        x0, y0, z0, qx0, qy0, qz0, qw0 = pose_to_list(actual)
        x1, y1, z1, qx1, qy1, qz1, qw1 = pose_to_list(goal)
        # Euclidean distance
        d = dist((x1, y1, z1), (x0, y0, z0))
        # phi = angle between orientations
        cos_phi_half = fabs(qx0 * qx1 + qy0 * qy1 + qz0 * qz1 + qw0 * qw1)
        return d <= tolerance and cos_phi_half >= cos(tolerance / 2.0)

    return True

robot_ip = "192.168.0.5"    # 예시 STEP IP 주소
robot_name = "NRMK-Indy7"   # IndyRP2의 경우 "NRMK-IndyRP2"
indy = client.IndyDCPClient(robot_ip, robot_name) # indy 객체 생성


indy.connect()
status = indy.get_robot_status()
print(status)
# if status['movedone']:
#     print("dafdsfasdfasdf")
# if status['collision']:
#         indy.set_robot_collision_level(0)
# print(status)
vel = 3
blend = 10

prog = JsonProgramComponent(policy=1, resume_time=2)  # Init. prgoram
joint_angles_1 = [0, 0, -90, 0, -90, 0]
joint_angles_2 = [0, 0, 0, 0, 0, 0]

# task_move_1 = [0,-0.1865,1.327,180,180,180]
t_pose = [0.5, -0.2, 0.3, 180, -10, 180]
t_pose1 = [0.68, -0.186, 0.648, 180, 90, 180]
home = [0.45, -0.186, 0.416, 180, 180, 180]
# prog.add_task_move_to(task_move_1, vel=vel, blend=blend)
# prog.add_task_move_to(t_pose1, vel=vel, blend=blend)
# prog.add_task_move_to(home, vel=vel, blend=blend)
# prog.add_joint_move_to(joint_angles_2, vel=vel, blend=blend)


prog_json = prog.program_done()  # Program end

indy.set_and_start_json_program(prog_json)  # Execute program

indy.disconnect()

