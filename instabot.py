import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv()
import time

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def login(browser):
    browser.get("https://www.instagram.com/?h1=en")
    time.sleep(20)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    login.click()
    
    time.sleep(20)

def visit_Tag(browser, url):
    sleepy_time = 20
    browser.get(url)
    time.sleep(20)

    pictures = browser.find_elements_by_css_selector("div[class='eLApa']")

    image_count = 0

    for picture in pictures:
        if image_count >= 3:
            break

        picture.click()
        time.sleep(sleepy_time)

        heart = browser.find_elements_by_css_selector("[aria-label='Like']")
        heart.click()

        close = browser.find_elements_by_css_selector("[aria-label='Close']")
        close.click()

        image_count += 1
    

def main():
    browser = webdriver.Firefox()
    login(browser)

    tags = [
        "programming",
        "freecodecamp",
        "_stitchesbyaisy_"
    ]

    while True:
        for tag in tags:
            visit_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(20)

main()
