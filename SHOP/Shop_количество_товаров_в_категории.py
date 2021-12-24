from selenium import webdriver

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

html = driver.find_element_by_xpath("//a[contains(text(), 'HTML')]")
html.click()

product = driver.find_elements_by_css_selector(css_selector=".product")
if len(product) == 3:
   print("Отображается 3 товара")
else:
   print("Ошибка. Количество товаров: " + str(len(items_count)))