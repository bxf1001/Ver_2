import pyautogui
import subprocess
import PySimpleGUI as sg
import time
import subprocess
import time
from pywinauto import Application
from pywinauto.keyboard import send_keys
from AppOpener import open, close

# Open WhatsApp




   #Add Number & Press F5

pyautogui.FailSafeException = False


def phone_number(number):
    open("Bandicam")
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

    #time.sleep(2)
    #pyautogui.hotkey('win', 'up')
#Start recording
    dialog = app.window(title="Video call ‎- WhatsApp")
    button = dialog.child_window(title="Add members", auto_id="ParticipantSideBarTriggerButton", control_type="Button")
    while True:
        try:
            if button.is_enabled():
                send_keys("{VK_F12}")
                break  # Button is enabled, so click it and exit the loop

#Puts First LK

        except:
            time.sleep(1)
            continue
        
    time.sleep(5)
    send_keys("^%{VK_NUMPAD0}")
#button_location1 = pyautogui.locateCenterOnScreen('end_button.png')

# Click the button
#time.sleep(0.5)
#pyautogui.click(button_location1)

def timer(timer):
#This is timer
    time.sleep(timer*60)
    try:
        app = Application(backend='uia').connect(title_re="WhatsApp") # Replace with the actual path
        app.Dialog.child_window(title="End call", auto_id="EndCallButton", control_type="Button").click()
    except:
        time.sleep(10)
        subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)
        
    if timer<9:
#Unlock 
        time.sleep(1)
        send_keys("^%{VK_NUMPAD0}")

#stop Recording
        time.sleep(2)
        send_keys("{VK_F12}")
#Final Lock
        time.sleep(2)
        send_keys("^%{VK_NUMPAD0}")


    
