# TestCaseTools Library
# Creating a library that can be imported to run test cases
# Samantha Panek
# August 22, 2016
#
#------------------------------------------------------------------------------

import pyautogui
import sys

# creates a function to be called checking whether an image is
# present on the user's screen
def imageDetection(imageLocation):
    coordinates= pyautogui.locateCenterOnScreen(imageLocation)
    if (coordinates is None):
        print ("Failed. Image not detected on screen.")
    else:
        print ("Pass. Image detected on screen.")
    return

# asks the user for their computer username to be called in other programs
def inputUsername():
    computerUsername= input("Enter your computer username as a string: ")
    return computerUsername

# has the program wait until a specified image has shown up on the screen
# before proceeding
def whileChecker(imageLocation):
    state= False
    while (state == False):
        coordinates= pyautogui.locateCenterOnScreen(imageLocation)
        if (coordinates is None):
            time.sleep(2)
        else:
            state= True
            time.sleep(2)
    return

# asks the user to check something (enter a requirement as checkStatement)
# on the current screen and press enter
def userCheck(checkStatement):
    try:
        input(checkStatement + " [Continue: Enter]")
    except SyntaxError:
        pass
    return

# checks whether a user ahs a mac or a pc
def computerChecker():
    if (sys.platform == "linux" or sys.platform == "linux2"):
        return "Linux"
    elif (sys.platform == "darwin"):
        return "Mac"
    elif (sys.platform == "win32"):
        return "PC"
    





            
