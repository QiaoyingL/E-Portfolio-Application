import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#################################################################################################
def test_login_fail(): #Invalid credentials
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("Adam")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Adam0921")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

###

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
#################################################################################################

#################################################################################################
def test_add_catCCA(): #Adding CCA category
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("qiaoying")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Password123")

    #Login
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(3)
    
    #Clicking Categorys
    driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a').click()
    time.sleep(3)

    #Clicking Add Catergory
    driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
    
    catName = driver.find_element_by_name("name")
    catName.clear()
    catName.send_keys("Hobby")

    driver.find_element_by_xpath('//*[@id="category_form"]/div/div/input[1]').click()

###

def test_add_catEmpty(): #Adding empty category
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("qiaoying")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Password123")

    #Login
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(3)
    
    #Clicking Categorys
    driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a').click()
    time.sleep(3)

    #Clicking Add Catergory
    driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
    
    catName = driver.find_element_by_name("name")
    catName.clear()
    catName.send_keys("")

    driver.find_element_by_xpath('//*[@id="category_form"]/div/div/input[1]').click()
#################################################################################################

#################################################################################################
def test_add_postCCA(): #Adding CCA Post
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("qiaoying")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Password123")

    #Login
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(3)
    
    #Clicking Posts
    driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a').click()
    time.sleep(3)

    #Clicking Add Post
    driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
    
    postName = driver.find_element_by_name("title")
    postName.clear()
    postName.send_keys("CCA")

    postBody = driver.find_element_by_name("body")
    postBody.clear()
    postBody.send_keys("What are the Co-Curricular Activities (CCA) that I have joined...")

    postCat = driver.find_element_by_name("categories")
    driver.find_element_by_xpath('//select[@id="id_categories"]/option[1]').click()    
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()

###

def test_add_emptyTitleCCA(): #Adding empty title CCA Post
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("qiaoying")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Password123")

    #Login
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(3)
    
    #Clicking Posts
    driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a').click()
    time.sleep(3)

    #Clicking Add Post
    driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
    
    postName = driver.find_element_by_name("title")
    postName.clear()
    postName.send_keys("")

    postBody = driver.find_element_by_name("body")
    postBody.clear()
    postBody.send_keys("What are the Co-Curricular Activities (CCA) that I have joined...")

    postBody = driver.find_element_by_name("categories")
    driver.find_element_by_xpath('//select[@id="id_categories"]/option[1]').click() 
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()

###

def test_add_emptyBodyCCA(): #Adding empty body CCA Post
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("qiaoying")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Password123")

    #Login
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(3)
    
    #Clicking Posts
    driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a').click()
    time.sleep(3)

    #Clicking Add Post
    driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
    
    postName = driver.find_element_by_name("title")
    postName.clear()
    postName.send_keys("CCA")

    postBody = driver.find_element_by_name("body")
    postBody.clear()
    postBody.send_keys("")

    postBody = driver.find_element_by_name("categories")
    driver.find_element_by_xpath('//select[@id="id_categories"]/option[1]').click()
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()

###

def test_add_emptyCatCCA(): #Adding empty Cat CCA Post
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("qiaoying")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("Password123")

    #Login
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(3)
    
    #Clicking Posts
    driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a').click()
    time.sleep(3)

    #Clicking Add Post
    driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
    
    postName = driver.find_element_by_name("title")
    postName.clear()
    postName.send_keys("CCA")

    postBody = driver.find_element_by_name("body")
    postBody.clear()
    postBody.send_keys("What are the Co-Curricular Activities (CCA) that I have joined...")

    postBody = driver.find_element_by_name("categories")
    driver.find_element_by_xpath('').click()
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()
#################################################################################################

#################################################################################################
def test_comment(): #Comment posted (Hobbies)
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/10/")

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("Gin")

    elemComment = driver.find_element_by_name("body")
    elemComment.send_keys("Interesting hobby!")

    elemName.send_keys(Keys.RETURN)

###

def test_comment_empty(): #Empty comment (Hobbies)
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/10/")

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("Janine")

    elemComment = driver.find_element_by_name("body")
    elemComment.send_keys("")

    elemName.send_keys(Keys.RETURN)
