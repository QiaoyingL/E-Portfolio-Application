import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

driver = webdriver.Chrome()
driver.get("http://localhost:8000/blog/")
driver.find_element_by_link_text("Projects done").click()

elemName = driver.find_element_by_name("author")
#elemName.send_keys("JJ")

#elemComment = driver.find_element_by_name("body")
#elemComment.send_keys("Hi!")

#elem.clear()
elemName.send_keys(Keys.RETURN)

