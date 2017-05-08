'''
pyAutoGUI TCs
Samantha Panek
'''

import pyautogui
import time
import sys
import os

import PoE

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()


count = int(sys.argv[1])


# 1 full cycle
def py_automation_gui():
    cycleCount= "%d" % x
        
	print(" ")
	print "Starting Cycle # %d " % x 
	print (time.strftime("%H:%M:%S"))

    # insert automation test case code here



        
        
	return
	
	
	




for x in range(1,count+10):
	#time.sleep(5)
	py_automation_gui()
	print "Cycle # %d complete" % x
	print (time.strftime("%H:%M:%S"))

exit()
	
	

#how we get time.sleep play nice with clicks 
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
