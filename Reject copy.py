import subprocess
from pywinauto import Application
from pywinauto.keyboard import send_keys
import PySimpleGUI as sg
import time
from whatsapp import WhatsApp
app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
time.sleep(3)
app = Application(backend='uia').connect(title_re="WhatsApp")
events=['"Group video call \u200e- WhatsAppDialog"', 'Dialog', 'Group video call \u200e- WhatsApp',
         'Group video call \u200e- WhatsAppDialog0','Group video call \u200e- WhatsAppDialog1',
          'Dialog0', 'Dialog1', 'Group video call \u200e- WhatsApp0', 
          'Group video call \u200e- WhatsApp1']

print(events[0])
for event in events:
    dialog = app.window(title=event, control_type="Window")
    button = dialog.child_window(title="Group video call ‎- WhatsApp", auto_id="TitleBar", control_type="Window")
    while True:
        try:
            if button.is_enabled():
                time.sleep(2) 
                sg.theme('NeutralBlue')
                layout=[sg.popup('Conference Not Allowed',font='stencil 50')]
                time.sleep(2)
                WhatsApp.click_end_button()
                WhatsApp.unlock_screen()
                WhatsApp.stop_recording()
                WhatsApp.lock_screen()
                break  # Button is enabled, so click it and exit the loop
        except:
            time.sleep(1)
            continue

#app.dialog.print_control_identifiers()
