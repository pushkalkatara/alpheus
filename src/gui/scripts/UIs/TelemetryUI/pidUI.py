#!/usr/bin/env python
try:
    from Tkinter import *
    import ttk
    import tkFont
except ImportError:
    from tkinter import *
    import ttk
    import tkinter.font as tkFont

import rospy
from alpheus_msgs.msg import pressurePID
from alpheus_msgs.msg import headingPID

class pidUI:
    def __init__(self, frameTele):
        rospy.Subscriber('/pressurePID', pressurePID, self.pressure_cb)
        rospy.Subscriber('/headingPID', headingPID, self.heading_cb)
        #Orientation
        frameOrientation = Frame(frameTele , bg='white')
        frameOrientation.grid(row=1, column=3, sticky=W, padx=15, pady=15)
        # grouping of widgets
        groupOrientation = LabelFrame(frameOrientation, text="PID",font="Times")
        groupOrientation.pack()
	    # widget definitions
        lblX = Label(groupOrientation, text="pKp:",font="Times")
        lblY = Label(groupOrientation, text="pKi:",font="Times")
        lblZ = Label(groupOrientation, text="pKd:",font="Times")
        lblhX = Label(groupOrientation, text="hKp:",font="Times")
        lblhY = Label(groupOrientation, text="hKi:",font="Times")
        lblhZ = Label(groupOrientation, text="hKd:",font="Times")

	    # declare and initialize variables
        self.vX = StringVar()
        self.vX.set("0")
        self.vY = StringVar()
        self.vY.set("0")
        self.vZ = StringVar()
        self.vZ.set("0")
        self.vhX = StringVar()
        self.vhX.set("0")
        self.vhY = StringVar()
        self.vhY.set("0")
        self.vhZ = StringVar()
        self.vhZ.set("0")
	    # associate variables with labels displaying data
        self.entXData = Entry(groupOrientation, textvariable=self.vX, background="blue",font="Times")
        self.entYData = Entry(groupOrientation, textvariable=self.vY, background="blue",font="Times")
        self.entZData = Entry(groupOrientation, textvariable=self.vZ, background="blue",font="Times")
        self.enthXData = Entry(groupOrientation, textvariable=self.vX, background="blue",font="Times")
        self.enthYData = Entry(groupOrientation, textvariable=self.vY, background="blue",font="Times")
        self.enthZData = Entry(groupOrientation, textvariable=self.vZ, background="blue",font="Times")
	    # layout widgets within group
        lblX.grid(row=0,sticky=W,padx=5,pady=5)
        lblY.grid(row=1,sticky=W,padx=5,pady=5)
        lblZ.grid(row=2,sticky=W,padx=5,pady=5)
        self.entXData.grid(row=0,column=1)
        self.entYData.grid(row=1,column=1)
        self.entZData.grid(row=2,column=1)
        lblhX.grid(row=3,sticky=W,padx=5,pady=5)
        lblhY.grid(row=4,sticky=W,padx=5,pady=5)
        lblhZ.grid(row=5,sticky=W,padx=5,pady=5)
        self.enthXData.grid(row=3,column=1)
        self.enthYData.grid(row=4,column=1)
        self.enthZData.grid(row=5,column=1)

    def pressure_cb(self, data):
        self.vX.set(str(data.pkp))
        self.vY.set(str(data.pki))
        self.vZ.set(str(data.pkd))

    def heading_cb(self, data):
        self.vhX.set(str(data.hkp))
        self.vhY.set(str(data.hki))
        self.vhZ.set(str(data.hkd))