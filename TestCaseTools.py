# TestCaseTools Library
# Creating a library that can be imported to run test cases
# Samantha Panek
# August 22, 2016
#
#------------------------------------------------------------------------------

import pyautogui

# creates a function to be called checking whether an image is
# present on the user's screen
def imageDetection(computerUsername):
    image= "/Users/" + computerUsername + "/Desktop/Capture.PNG"
    coordinates= pyautogui.locateCenterOnScreen(image)
    if (coordinates is None):
        print ("Failed. Image not detected on screen.")
    else:
        print ("Pass. Image detected on screen.")
    return

# asks the user for their computer user name to be called in other programs
def inputUsername():
    computerUsername= input("Enter your computer username as a string: ")
    return computerUsername

# has the program wait until a specified image has shown up on the screen
def whileChecker(imageTitle, computerUsername):
    image= "/Users/" + computerUsername + "/Desktop/" + imageTitle
    state= False
    while (state == False):
        coordinates= pyautogui.locateCenterOnScreen(image)
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




            
