from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://practice.automationtesting.in/')

my_account = driver.find_element_by_tag_name("[href='http://practice.automationtesting.in/my-account/']")
my_account.click()

username = driver.find_element_by_id("username")
username.send_keys("aya1@ya.ru")

password = driver.find_element_by_id("password")
password.send_keys("@vbccb!")

login_btn = driver.find_element_by_name("login")
login_btn.click()

shop = driver.find_element_by_xpath("//a[contains(text(), 'Shop')]")
shop.click()

android_quick = driver.find_element_by_xpath("//h3[contains(text(), 'Android Quick Start Guide')]")
android_quick.click()

old_price = driver.find_element_by_xpath("//del/span")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"

price = driver.find_element_by_xpath("//ins/span")
price_get_text = price.text
assert price_get_text == "₹450.00"

img = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.TAG_NAME, "[title='Android Quick Start Guide']")))
img.click()

close = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
close.click()

# driver.quit()