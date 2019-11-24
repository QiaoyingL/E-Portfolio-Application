import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login_fail(): #Invalid credentials
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("Janer")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Janer0921")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

def test_login_success(): #Valid credentials
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("qiaoying")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Password123")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
