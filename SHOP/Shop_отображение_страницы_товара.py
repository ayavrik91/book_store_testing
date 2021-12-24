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

html_5_forms = driver.find_element_by_xpath("//h3[contains(text(), 'HTML5 Forms')]")
html_5_forms.click()

html_5_forms_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "HTML5 Forms"))