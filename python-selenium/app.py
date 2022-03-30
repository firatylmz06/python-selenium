from selenium import webdriver
import time

browser = webdriver.Chrome("C:\\Users\\GITHUB\\Desktop\\chromedriver.exe")

browser.get("https://www.linkedin.com")

time.sleep(1)
browser.fullscreen_window()

login = browser.find_element_by_css_selector("body > nav > div > a.nav__button-secondary")
login.click()

time.sleep(2)

email_input = browser.find_element_by_xpath("//*[@id='username']")
password_input = browser.find_element_by_xpath("//*[@id='password']")

time.sleep(2)

email_input.send_keys("email@gmail.com")
password_input.send_keys("password")

time.sleep(2)

login = browser.find_element_by_css_selector("#organic-div > form > div.login__form_action_container > button")
login.click()
