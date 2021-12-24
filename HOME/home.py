from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

selenium_ruby = driver.find_element_by_xpath("//h3[contains(text(), 'Selenium Ruby')]")
selenium_ruby.click()

rewiews = driver.find_element_by_tag_name("[href='#tab-reviews']")
rewiews.click()

five = driver.find_element_by_class_name("star-5")
five.click()

comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")

name = driver.find_element_by_id("author")
name.send_keys("Ксюша")

email = driver.find_element_by_id("email")
email.send_keys("aya@ya.ru")

submit_btn = driver.find_element_by_id("submit")
submit_btn.click()