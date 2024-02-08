import pyautogui
import subprocess
import PySimpleGUI as sg
import time
import subprocess
import time
from pywinauto import Application


   #Add Number & Press F5

pyautogui.FailSafeException = False


def phone_number(number):
    app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
    time.sleep(2)
    app = Application(backend='uia').connect(title_re="WhatsApp") # Replace with the actual path
    
    url = f"whatsapp://send?phone=+91{number}"
    subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)
    time.sleep(0.25)
    subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)

    time.sleep(1)
    while True:
        try:
            app.WhatsAppDialog.child_window(title="Video call", auto_id="VideoCallButton", control_type="Button").click()
            break
        except:
            time.sleep(1)
            continue

    time.sleep(2)
    pyautogui.hotkey('win', 'up')
#Start recording
    try:
        while True:
            try:
                button_location = pyautogui.locateOnScreen('ringing.png')
                button_center = pyautogui.center(button_location)
                pyautogui.click(button_center.x, button_center.y)
                time.sleep(30)
                button_center = pyautogui.press("f12")
                break
            except:
                time.sleep(1)
                continue

#Puts First LK
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'alt', 'num0')
    except:
        time.sleep(1)
        subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)

#button_location1 = pyautogui.locateCenterOnScreen('end_button.png')

# Click the button
#time.sleep(0.5)
#pyautogui.click(button_location1)

def timer(timer_1):
#This is timer
    time.sleep(timer_1*60)
    try:
        app = Application(backend='uia').connect(title_re="WhatsApp") # Replace with the actual path
        app.Dialog.child_window(title="End call", auto_id="EndCallButton", control_type="Button").click()
    except:
        time.sleep(2)
        subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)

    if timer_1<9:
#Unlock 
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'alt', 'num0')

#stop Recording
        time.sleep(2)
        pyautogui.press('f12')
#Final Lock
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'alt', 'num0')


    
