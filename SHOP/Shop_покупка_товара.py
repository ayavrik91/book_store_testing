import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://practice.automationtesting.in/')

shop = driver.find_element_by_xpath("//a[contains(text(), 'Shop')]")
shop.click()

driver.execute_script("window.scrollBy(0, 300);")

html5_web_add = driver.find_element_by_tag_name('[data-product_id="182"]')
html5_web_add.click()

time.sleep(5)
cart_contents = driver.find_element_by_class_name("cartcontents")
cart_contents.click()

procced_to_checoud = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
procced_to_checoud.click()

first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Ксюша")

last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Каврегина")

email = driver.find_element_by_id("billing_email")
email.send_keys("aya@ya.ru")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("1234567890")

country_btn = driver.find_element_by_class_name("select2-choice")
country_btn.click()
country = driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Russia")
time.sleep(2)
country_ru = driver.find_element_by_class_name('select2-match')
country_ru.click()

address = driver.find_element_by_id("billing_address_1")
address.send_keys("Ленина, д.25, кв. 58")

city = driver.find_element_by_id("billing_city")
city.send_keys("Москва")

county = driver.find_element_by_id("billing_state")
county.send_keys("Россия")

zip = driver.find_element_by_id("billing_postcode")
zip.send_keys("404155")

driver.execute_script("window.scrollBy(0, 300);")

check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()

place_order = driver.find_element_by_id("place_order")
place_order.click()

thank_you_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

payment_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3)>td"), "Check Payments"))












