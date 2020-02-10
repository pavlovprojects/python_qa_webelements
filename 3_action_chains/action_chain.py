from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

chrome = webdriver.Chrome()
chrome.implicitly_wait(20)
chrome.maximize_window()
actions = ActionChains(chrome)

chrome.get("https://sketch.io/sketchpad/en/")
area = chrome.find_element_by_tag_name("sketch-viewport")
time.sleep(5)

actions.move_to_element_with_offset(area, random.randint(400, 600), random.randint(400, 600)).click_and_hold()
for i in range(10):
    actions.move_by_offset(random.randint(-100, 100), random.randint(-100, 100)).perform()
