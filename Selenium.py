from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://www.wikipedia.org/")
time.sleep(3)
link = driver.find_element_by_xpath('//*[@id="js-link-box-en"]')
link.click()
time.sleep(3)
searchBox = driver.find_element_by_id("searchInput")
searchBox.send_keys("Indian Police Service")
searchBox.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()
