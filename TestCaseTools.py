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

# asks the user for their computer user name to be called in other programs
def inputUsername():
    computerUsername= input("Enter your computer username as a string: ")
    return computerUsername
