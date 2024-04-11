import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://eprisons.nic.in/TamilNadu/Secure/Login.aspx')


# find username/email field and send the username itself to the input field

browser.find_element(By.ID, "txtUserid").send_keys("sppuzhal1")
# find password input field and insert password as well
browser.find_element(By.ID, "txtPassword").send_keys("sppuzhal11")
browser.find_element(By.ID, "btnLogin").click()
time.sleep(2)
browser.find_element(By.PARTIAL_LINK_TEXT, "Administration").click()
time.sleep(0.5)
browser.find_element(By.PARTIAL_LINK_TEXT, "Online Visit Approval").click()
time.sleep(3)

browser.find_element(By.XPATH, "//span[normalize-space()='Physical']").click()
time.sleep(0.5)
browser.find_element(By.XPATH, "//li[normalize-space()='VideoConferencing']").click()
time.sleep(0.5)
browser.find_element(By.XPATH, "//input[@id='ContentPlaceHolder1_ImageButton1']").click()
time.sleep(0.5)
browser.find_element(By.XPATH, "//div[@id='ContentPlaceHolder1_CalendarExtender1_day_2_4']").click()
time.sleep(0.5)
browser.find_element(By.XPATH, "//input[@id='ContentPlaceHolder1_txtDate']").click()
time.sleep(0.5)
browser.find_element(By.XPATH, "//input[@id='ContentPlaceHolder1_btnSearch']").click()
time.sleep(0.5)
time.sleep(100000) # sleep for 5 seconds so you can see the results
browser.quit()
