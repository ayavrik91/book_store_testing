import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://practice.automationtesting.in/')

shop = driver.find_element_by_xpath("//a[contains(text(), 'Shop')]")
shop.click()

driver.execute_script("window.scrollBy(0, 300);")
html5_web_add = driver.find_element_by_tag_name('[data-product_id="182"]')
html5_web_add.click()
time.sleep(3)
js_data_add = driver.find_element_by_tag_name('[data-product_id="180"]')
js_data_add.click()

cart_contents = driver.find_element_by_class_name("cartcontents")
cart_contents.click()

time.sleep(3)
delete = driver.find_element_by_tag_name('[data-product_id="182"]')
delete.click()

time.sleep(5)
undo = driver.find_element_by_xpath("//a[contains(text(), 'Undo')]")
undo.click()

quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
quantity.clear()
quantity.send_keys("3")

updata_basket = driver.find_element_by_name("update_cart")
updata_basket.click()

time.sleep(5)
quantity_js_data = driver.find_element_by_css_selector(css_selector='.cart_item:nth-child(1)>.product-quantity>.quantity>input')
quantity_js_data_value = quantity_js_data.get_attribute("value")
assert quantity_js_data_value == "3"

time.sleep(5)
apply_coupon_btn = driver.find_element_by_name("apply_coupon")
apply_coupon_btn.click()

time.sleep(5)
please = driver.find_element_by_css_selector(css_selector=".woocommerce-error>li")
please_text = please.text
assert please_text == "Please enter a coupon code."



driver.quit()