from selenium import webdriver

chrome = webdriver.Chrome(executable_path="drivers/chromedriver")
chrome.implicitly_wait(10)
chrome.get("https://yandex.ru")

home_tabs = chrome.find_element_by_css_selector(".home-tabs3")
search_input = chrome.find_element_by_css_selector("input#text")

chrome.close()
