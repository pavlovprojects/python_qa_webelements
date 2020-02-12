from selenium.webdriver import ActionChains
from selenium import webdriver
import random
import time

chrome = webdriver.Chrome(executable_path="../../Env/drivers/chromedriver")
chrome.implicitly_wait(20)
chrome.maximize_window()
actions = ActionChains(chrome)

chrome.get("https://sketch.io/sketchpad/en/")
area = chrome.find_element_by_tag_name("sketch-viewport")

time.sleep(5) # Нужно убрать модалку

for i in range(15):
    actions.move_to_element_with_offset(area, random.randint(400, 600), random.randint(400, 600)).click_and_hold()
    actions.move_by_offset(random.randint(-150, 150), random.randint(-150, 150)).release()
actions.perform()
