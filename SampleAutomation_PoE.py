'''
August 22, 2016
PoE Library 
CREE
Samantha Panek
'''

import pyautogui
import time
import sys
import os

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()


# continuously checks for an image on a screen and continues when it does
def whileChecker(imageLocation):
    state= False
    while (state == False):
        coor1= pyautogui.locateCenterOnScreen(imageLocation)
        if (coor1 is None):
            pyautogui.click(996, 275)
            time.sleep(5)
        else:
            time.sleep(1)
            state= True
    return

# continuously checks for either one of the images to show up and continues
# when one shows up on the screen
def whileChecker2(imageLocation1, imageLocation2):
    state = False
    while (state == False):
        coor1 = pyautogui.locateCenterOnScreen(imageLocation1)
        coor2 = pyautogui.locateCenterOnScreen(imageLocation2)
        if ((coor1 is None) and (coor2 is None)):
            pyautogui.click(996, 275)
        else:
            state= True
    return

# while checker for when using automation with Wireshark. Checks for two
# images constantly and when it finds one, it returns center coordinates
def whileCheckerClickWireshark(imageLocation1, imageLocation2):
    state= False
    while (state == False):
        coor1= pyautogui.locateCenterOnScreen(imageLocation1)
        coor2= pyautogui.locateCenterOnScreen(imageLocation2)
        if ((coor1 is None) and (coor2 is None)):
            continue
        else:
            state= True
        if (coor1 is None):
            location = coor2
            else:
            location = coor1
    return location

# checks for a specific image to show up on the screen and when it does it
# returns the location of the image so that it can be clicked on within a TC
def whileCheckerClick(imageLocation):
    state= False
    while (state == False):
        coor1= pyautogui.locateCenterOnScreen(imageLocation)
        if (coor1 is None):
            continue
        else:
                state= True
    return pyautogui.locateCenterOnScreen(imageLocation)

# takes a screenshot and saves it to the screenshots folder on the users Desktop
# the image is time stamped in the name
def screenshots(cycleCount):
    imageTitle= "\Users\spanek\Desktop\Screenshots\Screenshot Cycle" + cycleCount + " " + time.strftime("%m%d%y %H%M%S") + ".png" 
    img= pyautogui.screenshot()
    img.save(imageTitle)
    print ("Took Screenshot")
    return

# checks for a certain image on the and prints a pass/fail of whether it was found
def imageDetection(imageTitle):
	location= "\Users\spanek\Desktop"
	image= os.path.join(location, imageTitle)
    coor= pyautogui.locateCenterOnScreen(image)
    if (coor is None):
        print ("Failed")
    else:
        print ("Passed")
    return

# askes the user to check something (statement) on the screen then press enter
# to continue running the rest of the code
def userCheck(checkStatement):
    try:
        input(checkStatement + " [Continue: Enter]")
    except SyntaxError:
        pass
    return

# opens and closes SCM given the number of times you'd like to open and close it
# and the image it is looking for upon reopening the SCM
def openAndClose(count, imageTitle):
    for x in range(1,count+1):
        # close SCM
        pyautogui.moveTo(1895,9) 
        pyautogui.click() 
        print("Closed SCM")
        time.sleep(2)

        # reopen SCM
        pyautogui.hotkey('win')
        pyautogui.typewrite('Cree SmartCast Manager')
        time.sleep(3)
        pyautogui.hotkey('enter')
        print("Opened SCM")
        time.sleep(30)

        #check for correct image on screen
        imageDetection(imageTitle)
    return

#completes a factory reset before OBS has completed (devices unassigned)
def factoryResetPreOBS():
    #open settings
	pyautogui.moveTo(1024,65) 
    pyautogui.click() 
	print("Opened Settings tab")
	time.sleep(5)

	#clicked the Network devices
	pyautogui.moveTo(165,1003) 
    pyautogui.click() 
	print("Clicked the Network")
	time.sleep(5)

	#select factory reset
	pyautogui.moveTo(1562,234) 
    pyautogui.click()
	print("Selected Factory Reset for all devices")
	time.sleep(2)
	
	#click yes
	pyautogui.press('enter')
	print("Clicked Yes")
	time.sleep(.5)
	
	#click ok
	pyautogui.press('enter')
	print("Clicked OK")
	time.sleep(120)

	return
	

#completes a factory reset after OBS has completed (devices in Network)     
def factoryResetPostOBS():
    #open settings
	pyautogui.moveTo(1024,65) 
    pyautogui.click() 
	print("Opened Settings tab")
	time.sleep(5)

	#clicked all devices
	pyautogui.moveTo(953,130) 
    pyautogui.click() 
	print("Clicked All Devices")
	time.sleep(5)

	#select factory reset
	pyautogui.moveTo(1650,232) 
    pyautogui.click()
	print("Selected Factory Reset for all devices")
	time.sleep(2)
	
	#clickyes
	pyautogui.press('enter')
	print("Clicked Yes")
	time.sleep(.5)
	
	#click ok
	pyautogui.press('enter')
	print("Clicked OK")
	i = 24
	while i>=0:
        pyautogui.click(996, 275)
        time.sleep(5)
        i = i - 1

	return
                
# Runs a OneButton Setup and commissions the lighting network
def obs(cycleCount):
	#factory resrtting all devices
    factoryResetPostOBS()

    #check for all devices returned
	imageDetection("Capture1.PNG")        
        
	#select obs
	pyautogui.moveTo(1233, 66) 
    pyautogui.click()
	print("Opened OBS tab")
	time.sleep(2)
	
	#select all devices
	pyautogui.moveTo(965, 586) 
    pyautogui.click()
	print("Selected ALL devices")
        
    #checking for OK button
    whileChecker2("\Users\spanek\Desktop\AutoTCs\ImagesForOBS\OK.PNG",
                  "\Users\spanek\Desktop\AutoTCs\ImagesForOBS\OK1.PNG")

    #take screenshot
    screenshots(cycleCount)
    time.sleep(.5)
        
	#ok
	pyautogui.moveTo(947, 592) 
    pyautogui.click()
	print("Selected OK")
	time.sleep(1.5)

	#check for network
	imageDetection("Capture.PNG")
                
	return

#opens and starts a wireshark
def startWireshark(cycleCount):
        # opens wireshark throught the start menu
        pyautogui.hotkey('win')
        pyautogui.typewrite('Wireshark')
        time.sleep(1)
        pyautogui.hotkey('enter')
        print ("Opened Wireshark")

        # clicks on the local area connection
        locationLocal = whileCheckerClick("\Users\spanek\Desktop\AutoTCs\ImagesForOBS\Local.PNG")
        pyautogui.click(locationLocal)
        print ("Opened Local Area Connection")

        # starts the wireshark for the local area connection
        locationStart = whileCheckerClick("\Users\spanek\Desktop\AutoTCs\ImagesForOBS\StartWireshark.PNG")
        pyautogui.click(locationStart)
        print ("Started Wireshark")
        time.sleep(1)

        # minimizes wireshark
        pyautogui.hotkey('win', 'down')

        return

#stops and saves wireshark logs and graphs
def stopWireshark(cycleCount):
        # reopens wireshark from the task bar
        locationWireshark2 = whileCheckerClick("\Users\spanek\Desktop\AutoTCS\ImagesForOBS\Wireshark2.PNG")
        pyautogui.click(locationWireshark2)
        print ("Reopened Wireshark")

        # stops the wireshark
        locationStop = whileCheckerClick("\Users\spanek\Desktop\AutoTCS\ImagesForOBS\StopWireshark.PNG")
        pyautogui.click(locationStop)
        print ("Stopped Wireshark")
        time.sleep(1)

        # opens the save window
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1.5)

        # checks if this is the first cycle of saving the wireshark and
        # if so opens the desktop wireshark file folder
        if (cycleCount == "1"):
            locationDesktop = whileCheckerClick("\Users\spanek\Desktop\AutoTCS\ImagesForOBS\Desktop.PNG")
            pyautogui.click(locationDesktop)

            locationFolder = whileCheckerClickWireshark("\Users\spanek\Desktop\AutoTCS\ImagesForOBS\Folder.PNG",
                                                        "\Users\spanek\Desktop\AutoTCS\ImagesForOBS\Folder2.PNG")
            pyautogui.doubleClick(locationFolder)
            locationSaveBox = whileCheckerClick("\Users\spanek\Desktop\AutoTCS\ImagesForOBS\SaveBox.PNG")
            pyautogui.click(locationSaveBox)

        # saves the month, day, year, hour, minute, and second to timestamp the wireshark
        m = time.strftime("%m")
        d = time.strftime("%d")
        y= time.strftime("%y")
        hr = time.strftime("%H")
        minu = time.strftime("%M")
        sec =time.strftime("%S")

        #saves the wireshark log with the timestamp
        pyautogui.typewrite('log' + cycleCount + "_" + m + d + y + "_" + hr + minu + sec)
        time.sleep(1)
        pyautogui.press('enter')
        print ("Saved Wireshark log")

        # opens the wireshark IO graph
        locationStatistics = whileCheckerClick("\Users\spanek\Desktop\AutoTCS\ImagesForOBS\Statistics.PNG")
        pyautogui.click(locationStatistics)
        time.sleep(1)
        pyautogui.moveRel(0, 167)
        pyautogui.click()
        time.sleep(2)

        #opens the save window
        pyautogui.hotkey('enter')
        time.sleep(.5)

        #saves the IO graph with the timestamp
        pyautogui.typewrite('graph' + cycleCount + "_" + m + d + y + "_" + hr + minu + sec)
        time.sleep(1)
        pyautogui.press('enter')
        print ("Saved Wireshark graph")
        time.sleep(5)

        #closes the IO graph the wireshark log windows
        print ("Closing Wireshark")
        pyautogui.hotkey('alt', 'f4')
        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(2)

        return
        
        

# Runs a OneButton Setup and opens and starts Wireshark
def obsWireshark(cycleCount):
    #factory resrtting all devices
    factoryResetPostOBS()

    #open and start wireshark
    startWireshark(cycleCount)

    #click on SCM window
    pyautogui.moveTo(1000, 6) 
    pyautogui.click()
    time.sleep(.5)

    #select obs
	pyautogui.moveTo(1233, 66) 
    pyautogui.click()
	print("Opened OBS tab")
	time.sleep(2)
	
	#select all devices
	pyautogui.moveTo(965, 586) 
    pyautogui.click()
	print("Selected ALL devices")
        
    #checking for OK button
    whileChecker2("\Users\spanek\Desktop\AutoTCs\ImagesForOBS\OK.PNG", "\Users\spanek\Desktop\AutoTCs\ImagesForOBS\OK1.PNG")

    #take screenshot
    screenshots(cycleCount)
    time.sleep(1)
        
	#ok
	pyautogui.moveTo(947,592) 
    pyautogui.click()
	print("Selected OK")
	time.sleep(1)

	#check for network
	imageDetection("Capture.PNG")
                
	return

def occSettings(taskTune, occTimeout, occLevel, unoccLevel, daylightEnDis,
                minDaylight):
    #change occ settings
	print("Changing Settings")

	#change task tune level
    print(" Task Tune Level= " + taskTune)
    pyautogui.moveTo(300, 280) 
    pyautogui.click() 
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(taskTune)

	#click save
    time.sleep(1)
	pyautogui.moveTo(90, 326) 
    pyautogui.click() 

	#change occ timeout
	print(" Occupancy Timeout= " + occTimeout)
	pyautogui.moveTo(300, 424) 
    pyautogui.click()
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.typewrite(occTimeout)

    #change occ level
	print(" Occupied Level= " + occLevel)
	pyautogui.moveTo(300, 467) 
    pyautogui.click()
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.typewrite(occLevel)

	#change unocc level
	print(" Unoccupied Level= " + unoccLevel)
	pyautogui.moveTo(300, 507) 
    pyautogui.click()
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.typewrite(unoccLevel)

	#click submit
	time.sleep(1)
	pyautogui.moveTo(83, 595) 
    pyautogui.click() 

	#change daylighting enable/disable
    enDis= daylightEnDis.lower()        
    if (enDis == "disable" or enDis == "dis" or enDis == "d"):
        print(" Daylighting Disabled")
        pyautogui.moveTo(369,699)
        pyautogui.click()
    else:
        print(" Daylighting Enabled")
        pyautogui.moveTo(275,698)
        pyautogui.click()

	#change min daylight
    print(" Mininimum Daylight Level= " + minDaylight)
	pyautogui.moveTo(300, 758) 
    pyautogui.click()
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.typewrite(minDaylight)

	#click save
	time.sleep(1)
	pyautogui.moveTo(83, 809) 
    pyautogui.click() 

	return
        


#how we get time.sleep play nice with clicks 
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
