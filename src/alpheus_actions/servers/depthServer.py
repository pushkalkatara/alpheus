#! /usr/bin/env python

'''
This receives offsetX from task server and 
'''
import rospy
import actionlib
import alpheus_actions.msg
from alpheus_msgs.msg import pressure, offsetData

class depthAction(object):
    _feedback = alpheus_actions.msg.depthFeedback()
    _result = alpheus_actions.msg.depthResult()

    def __init__(self, name):
        self.pub = rospy.Publisher('/offsetData', offsetData, queue_size=10)
        rospy.Subscriber("/pressure", pressure, self.pressure_cb)
        self._da = name
        self._ds = actionlib.SimpleActionServer(
            self._da, \
            alpheus_actions.msg.depthAction, \
            execute_cb = self.depthCallback, \
            auto_start = False)
        self._ds.start()

    def pressure_cb(self, data):
        self._pressure = data.pressure

    def depthCallback(self, goal):
        r = rospy.Rate(10)
        success = True
        od = offsetData()
        od.offsetY = goal.depth_setpoint
        od.offsetX = 0
        while(goal.depth_setpoint != self._pressure):
            self.pub.publish(od)
            if self._ds.is_preempt_requested():
                rospy.loginfo('%s : Preempted' % self._da)
                self._ds.set_preempted()
                success = False
                break
            self._feedback.depth_error = self._pressure
            self._ds.publish_feedback(self._feedback)
            self._feedback.depth_error = self._pressure - goal.depth_setpoint
            rospy.loginfo('%s : Going to Pressure %f with Error : %f',\
                self._da , \
                goal.depth_setpoint, \
                self._feedback.depth_error)
            r.sleep()

        if success:
            self._result.depth_final = self._feedback.depth_error
            rospy.loginfo('%s : Success' % self._da)
            self._ds.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('depthServer')
    server = depthAction(rospy.get_name())
    rospy.spin()
