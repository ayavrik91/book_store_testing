from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://practice.automationtesting.in/')

shop = driver.find_element_by_xpath("//a[contains(text(), 'Shop')]")
shop.click()

html5_web = driver.find_element_by_xpath("//h3[contains(text(), 'HTML5 WebApp Develpment')]")
html5_web.click()
add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button")
add_to_basket.click()

cart_contents = driver.find_element_by_class_name("cartcontents")
cart_contents_get_text = cart_contents.text
assert cart_contents_get_text == "1 Item"

amount = driver.find_element_by_css_selector(css_selector=".wpmenucart-contents>.amount")
amount_get_text = amount.text
assert amount_get_text == "₹180.00"

cart = driver.find_element_by_class_name("cartcontents")
cart.click()

subtotal = WebDriverWait(driver, 5)
subtotal.until(EC.text_to_be_present_in_element((By.TAG_NAME, "[data-title='Subtotal']"), "₹180.00"))

total = WebDriverWait(driver, 5)
total.until(EC.text_to_be_present_in_element((By.XPATH, "//strong/span"), "₹189.00"))

