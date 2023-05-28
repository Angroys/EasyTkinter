from tkinter import *


class Frames:
    """
    Left Menu Bar

    :param width: The width of the frame
    :type width: int
    :return: Width of the frame

    :param height: The height of the frame
    :type height: int
    :return: Height of the frame

    :param color: The color of the frame
    :type color: string
    :return: Color of the frame

    :param tkinterRootWindow: The window the frame will be added
    :return:Frame

    
    """


    def __init__(self, tkinterRootWindow, width = 300, height = 300, color="green"):
        self.frameWidth = width
        self.frameHeight = height
        self.frameColor = color
        self.tkinterRootWindow = tkinterRootWindow
        self.createMenuBarFrame()
        self.setUpFrameGrid()
        self.frame.pack()

    
    def createMenuBarFrame(self):
        self.frame = Frame(master = self.tkinterRootWindow, bg= self.frameColor, width=self.frameWidth, height=self.frameHeight)
    

    def setUpFrameGrid(self):
        self.frame.grid(row=0,column=0, sticky="W")