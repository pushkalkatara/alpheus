#! /usr/bin/env python
from __future__ import print_function
import rospy
import actionlib
import alpheus_actions.msg

def taskClient():
    client = actionlib.SimpleActionClient('taskServer', alpheus_actions.msg.taskAction)
    client.wait_for_Server()
    goal = alpheus_actions.msg.taskGoal()
