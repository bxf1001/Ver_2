from pywinauto import Application
from pywinauto.keyboard import send_keys
import warning_label
import time
app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)

app = Application(backend='uia').connect(title_re="WhatsApp")
dialog = app.window(title="Group video call \u200e- WhatsApp")
button = dialog.child_window(title="Group video call ‎- WhatsAApp", auto_id="TitleBar", control_type="Window")
#app.dialog.print_control_identifiers()
while True:
    try:
        if button.is_enabled():
            time.sleep(2)
            app.Dialog.child_window(title="End call", auto_id="EndCallButton", control_type="Button").click()
            warning_label.show_warning()
            time.sleep(2)
            send_keys("{VK_F12}")
            break  # Button is enabled, so click it and exit the loop

#Puts First LK

    except:
        time.sleep(1)
        continue

app.dialog.print_control_identifiers()
