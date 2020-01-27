'''
Description:
Python 3 code to automatically download today's Times of India E-Paper 
Bengaluru Edition as a PDF
The program uses selenium and has been written for a Chrome webdriver
The PDF is downloaded to the default downloads folder specified in your browser
Code was tested on a Chrome browser installed on a MAC
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import os
import time

# Get today's date and store the individual day, month and year
now = datetime.datetime.now()
year = str(now.year)
month = str(now.month) if len(str(now.month)) == 2 else "0" + str(now.month)
day = str(now.day) if len(str(now.day)) == 2 else "0" + str(now.day)

# Path of your chrome driver - make sure the version matches your chrome browser version
CHROMEDRIVER_PATH = '/Users/tebbythomas/Downloads/chromedriver'

# Main login screen of TOI e-paper landing page
TOI_EPAPER_URL = "https://epaper.timesgroup.com/TOI/TimesOfIndia/Indialogin.aspx#"

# TOI Bengaluru edition main page post login
TOI_EPAPER_BLORE_URL = "https://epaper.timesgroup.com/olive/ODN/TimesOfIndia/Default.aspx#publication=TOIBG"

# Selenium code to access the chrome driver
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
# Opens the browser to the main login screen
driver.get(TOI_EPAPER_URL)
print("Accessed the login screen")
# Used later to access element using coordinates
actions = ActionChains(driver)
# Sleep functions used to wait for page elements to render
time.sleep(3)
# Loads JS script to render login frame on page
driver.execute_script("plenigo.login(configuration);")
time.sleep(2)
# Switches to login frame
print("Switching to login frame")
driver.switch_to.frame("plenigoFrameoverlay")
time.sleep(3)
# Passing the login credentials and clicking login button
driver.find_element_by_id("email").send_keys(os.environ['EMAIL_USER'])
driver.find_element_by_id ("password").send_keys(os.environ['TOI_LOGIN_PASSWORD'])
driver.find_element_by_css_selector(".btn-default[value='Log In']").click()
print("Succesfully logged in")
time.sleep(3)
# Switching to the main page
driver.switch_to.default_content()
time.sleep(3)
# Accessing the main TOI Bengaluru page
driver.get(TOI_EPAPER_BLORE_URL)
print("Accessed the Times of India Bengaluru page screen")
time.sleep(10)
# Setting the cursor to access the Save and downlaod PDF buttons on the page
# Unable to access the HTML elements themselves hence using this method 
print("Accessing the Download PDF button")
e = driver.find_element_by_id("toolbar")
time.sleep(3)
actions.move_to_element_with_offset(e, 900,10)
actions.move_by_offset(0, 0).click().perform()
actions.move_to_element_with_offset(e, 900,175)
time.sleep(3)
actions.move_by_offset(0, 0).click().perform()
print("PDF downloaded to the default download folder as set in Chrome")