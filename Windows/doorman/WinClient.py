import subprocess
import pyautogui

def autounlock():
    try:
        pyautogui.FAILSAFE = False
        #Search and locate the password input box
        pyautogui.click(1025,513, 2)
        #auto enter password
        pyautogui.typewrite("<TestPasswordHere>;'",2)
        #press the bottom
        pyautogui.press('enter')
    except:
        pass
     # Run this script after login.
    subprocess.call([r'<our future script, the lock screen lisener>'])


while <replace to socket unlock sign later> {
    autounlock()
    }
