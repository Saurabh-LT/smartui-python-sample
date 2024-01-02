from lambdatest_selenium_driver import smartui_snapshot
from selenium import webdriver


driver = webdriver.Chrome()
try:
    print('driver started')
    driver.get('https://www.pinterest.com/pin/16958936087791895/')
    smartui_snapshot(driver,"SS-1")
except Exception as err:
    print(err)
finally: 
    driver.close()
