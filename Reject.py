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
            dialog.child_window(title="End call", auto_id="EndCallButton", control_type="Button").click()
            time.sleep(1)
            sg.theme('NeutralBlue')
            layout=[sg.popup('Conference Not Allowed',font='stencil 50')]


            send_keys("{VK_F12}")
            break  # Button is enabled, so click it and exit the loop

#Puts First LK

    except:
        time.sleep(1)
        continue

