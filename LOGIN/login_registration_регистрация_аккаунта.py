from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://practice.automationtesting.in/')
time.sleep(5)

my_account = driver.find_element_by_tag_name("[href='http://practice.automationtesting.in/my-account/']")
my_account.click()

reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("aya1@ya.ru")
time.sleep(3)
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("@vbccb!")

register_btn = driver.find_element_by_name("register")
register_btn.click()


