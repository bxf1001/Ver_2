import time
from pywinauto import Application

app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
time.sleep(2)
app = Application(backend='uia').connect(title_re="WhatsApp") # Replace with the actual path
time.sleep(5)
app.WhatsAppDialog.child_window(title="Video call", auto_id="VideoCallButton", control_type="Button").click()
# Replace "Your Dialog Name" with the actual name of your dialog
dialog = app.window(title="Video call ‎- WhatsApp")

# Print the control identifiers for the dialog
#dialog.print_control_identifiers()
button = dialog.child_window(title="Add members", auto_id="ParticipantSideBarTriggerButton", control_type="Button")
#button = app.Dialog1.child_window(title="Add people")

# Define a timeout (in seconds) for waiting
timeout = 10

# Loop until the button is enabled or the timeout is reached
while True:
    try:
        if button.is_enabled():
            button.send_key('F12')
            break  # Button is enabled, so click it and exit the loop
    except TimeoutError:
        print("Button is still not enabled. Waiting...")
        # Sleep for a short interval before checking again
        time.sleep(1)