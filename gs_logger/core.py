#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from rospy import ServiceProxy,Subscriber
from std_msgs.msg import String
from gs_interfaces.srv import Log

class Logger():
    def __callback(self,data):
        self.__msg=data.data

    def __init__(self):
        self.__msg=""
        rospy.wait_for_service("geoscan/get_log")
        rospy.wait_for_message("geoscan/log",String)
        self.__log_service=ServiceProxy("geoscan/get_log",Log)
        self.__log_sub=Subscriber("geoscan/log",String,self.__callback)

    def lastMsgs(self):
        return self.__msg
    
    def allMsgs(self):
        return self.__log_service().msgs
