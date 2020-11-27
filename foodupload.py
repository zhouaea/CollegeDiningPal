from selenium import webdriver
import time

# Change the destination path and change variable browser to driver
browser = webdriver.Chrome('/Users/sammylee/Downloads/chromedriver');

webgate1 = browser.get('https://www.myfitnesspal.com/food/submit?date=2020-11-14&meal=0')

username_input = '//*[@id="username"]'
password_input = '//*[@id="password"]'
login_submit = ''
login_submit = '//*[@id="content"]/form/div/ul/li[5]/input'

# Change it to your account for fitness pal
browser.find_element_by_xpath(username_input).send_keys("Neo's email")
browser.find_element_by_xpath(password_input).send_keys("Neo's password")
browser.find_element_by_xpath(login_submit).click()
# browser.execute_script("document.querySelector('#cookies-select-all').click();")

res_input = '//*[@id="food_brand"]'
foodname_input = '//*[@id="food_description"]'
contin_submit = '//*[@id="buttonPad"]/input'
browser.find_element_by_xpath(res_input).clear()
browser.find_element_by_xpath(foodname_input).clear()
browser.find_element_by_xpath(res_input).send_keys("BC Dining")
# Change the food name for manipulation and testing purposes
browser.find_element_by_xpath(foodname_input).send_keys("Potatoe")
browser.find_element_by_xpath(contin_submit).click()

text = 'We think the food you submitted may already be in our database'
if text in browser.page_source:
    browser.execute_script("document.querySelector('.button').click()")



