from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
MY_EMAIL = "LINKEDIN_EMAIL"
PASSWORD = "PASSWORD"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=URL)

signup_button = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
signup_button.click()

time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys(MY_EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
sign_in_button = driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
sign_in_button.click()

apply = driver.find_element_by_css_selector(".jobs-s-apply button")
apply.click()

time.sleep(5)

phone_input = driver.find_element_by_css_selector(".fb-single-line-text__input")
phone_input.send_keys("Phone_Number")

time.sleep(5)

close_button = driver.find_element_by_css_selector('.artdeco-modal__dismiss')
close_button.click()

time.sleep(1)

discard = driver.find_element_by_css_selector('.artdeco-modal__confirm-dialog-btn')
discard.click()

time.sleep(3)

driver.get(url="https://www.linkedin.com/m/logout/")

time.sleep(3)

driver.quit()
