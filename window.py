from tkinter import *
from PIL import ImageTk, Image





class Window:
    """
    Main window class
    Window will be created with blank background firstly

    :param title: The Name of the Window
    :type title: str
    :return: Title of the window 

    :param width: The width of the window
    :type width: int
    :return: Width of the window

    :param height: The height of the window
    :type height: int
    :return: Height of the window

    :param columns: Number of columns of the grid
    :type columns: int

    :param rows: Number of rows of the grid
    :type rows: int

    
    """


    def __init__(self,title="Default", width=400, height=300, image=None):
    
        """
        Default window title is set to "Default", You shoud changee it
        Window default width is 400
        Window default height is 300
        """
        self.width = width
        self.height = height
        self.defaultWindowIconImage = image
        self.setupMainWindowAttributes(title)
        self.setupMainWindowDesignAttributes()

        

    def createTkinterWindow(self):
        
        self.tkinterWindow = Tk()



    def startTkinterWindow(self):
        self.tkinterWindow.mainloop()



    
    def centerTkinterWindowOnTheScreen(self):
        self.windowCenterOnXCoordinates = self.tkinterWindow.winfo_screenwidth() // 2 - self.width // 2
        self.windowCenterOnYCoordinates = self.tkinterWindow.winfo_screenheight() // 2 - self.height // 2
        



    def setTkinterWindowIconImage(self, image=None):
        self.tkinterWindow.wm_iconphoto(False, image)
    
    def setTkinterWindowTitle(self, windowTitle):
        self.tkinterWindow.title(windowTitle)

    
    
    def setUpTkinterWindowGeometry(self):
        self.centerTkinterWindowOnTheScreen()
        self.tkinterWindow.geometry(str(self.width) + "x"  + str(self.height) + "+" + str(self.windowCenterOnXCoordinates)+ "+" + str(self.windowCenterOnYCoordinates))

    def setupMainWindowDesignAttributes(self, image=None):
        if(image != None):
            self.setTkinterWindowIconImage(self.defaultWindowIconImage)
    
    
    def setupMainWindowAttributes(self, title):
        self.createTkinterWindow()
        self.setTkinterWindowTitle(title)
        self.setUpTkinterWindowGeometry()
        self.setUpTkinterWindowGridForFrames()


    def setUpTkinterWindowGridForFrames(self):
        Grid.rowconfigure(self.tkinterWindow,0,weight=1)
        Grid.columnconfigure(self.tkinterWindow,0,weight=1)    
        Grid.rowconfigure(self.tkinterWindow,1,weight=1)

    
    
    def getTkinterWindow(self):
        return self.tkinterWindow
    
    def getTkinterWindowHeight(self):
        return self.tkinterWindow.winfo_height()
    

    





