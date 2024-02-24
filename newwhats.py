import pyautogui
import subprocess
import PySimpleGUI as sg
import time
import subprocess
import time
from pywinauto import Application
from pywinauto.keyboard import send_keys
from AppOpener import open


class WhatsApp:


    def __init__(self,timer,number):
        self.timer = timer
        self.number=number
        self.startapp = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
        self.appwhatsapp = Application(backend='uia').connect(title_re="WhatsApp")
        self.runbandicam=open("Bandicam")
        self.url = f"whatsapp://send?phone=+91{number}"
        self.subwhatsapp=subprocess.Popen(["cmd", "/C", f"start {self.url}"], shell=True)
        self.detect_rec=self.appwhatsapp.WhatsAppDialog.child_window(title="Video call", auto_id="VideoCallButton", control_type="Button").click()
        self.videodialog = self.appwhatsapp.window(title="Video call ‎- WhatsApp")
        self.trigrec = self.videodialog.child_window(title="Add members", auto_id="ParticipantSideBarTriggerButton", control_type="Button")
        self.endcall=self.appwhatsapp.Dialog.child_window(title="End call", auto_id="EndCallButton", control_type="Button").click()
        self.killemergency=subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)

    def start_applications(self):
        self.startapp()
        self.appwhatsapp()
        self.runbandicam()
        self.url()
        self.subwhatsapp()


    def run_method(self):

    def _precheckevents_(self):

    def _postcheckevents_(self):
