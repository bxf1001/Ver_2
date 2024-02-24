import subprocess
from pywinauto import Application
from pywinauto.keyboard import send_keys
import PySimpleGUI as sg
import time
app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
time.sleep(3)
app = Application(backend='uia').connect(title_re="WhatsApp")
dialog = app.window(title="Group video call ‎- WhatsApp")

#app.dialog.print_control_identifiers()
while True:
    try:
        if dialog.is_enabled():
            time.sleep(2) 
            sg.theme('NeutralBlue')
            layout=[sg.popup('Conference Not Allowed',font='stencil 50')]
            time.sleep(2)
            subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)
            send_keys("^%{VK_NUMPAD0}")
            send_keys("{VK_F12}")
            send_keys("^%{VK_NUMPAD0}")
            break  # Button is enabled, so click it and exit the loop

#Puts First LK

    except:
        time.sleep(1)
        continue
