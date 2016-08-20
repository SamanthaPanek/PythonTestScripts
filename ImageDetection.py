# PythonTestScripts
# ImageDetection
# Samantha Panek
# August 19, 2016

# Directions:
# Use snipping tool or take a screenshot and save the file as
# Capture.PNG located on your desktop
# **Note: if you'd like to test this, remove the # from the last
#         line of code
# ------------------------------------------------------------


import pyautogui
import time
import InputUsername

# creates a function to be called checking whether an image is
# present on the user's screen
def ImageDetection(computerUsername):
    image= "/Users/" + computerUsername + "/Desktop/Capture.PNG"
    coordinates= pyautogui.locateCenterOnScreen(image)
    if (coordinates is None):
        print ("Failed. Image not detected on screen.")
    else:
        print ("Pass. Image detected on screen.")

# calls the inputUsername function to ask the user for their
# computer username
inputComputerUsername= InputUsername.inputUsername()

# runs the ImageDetection fuction for the computer username
# ImageDetection(inputComputerUsername)
