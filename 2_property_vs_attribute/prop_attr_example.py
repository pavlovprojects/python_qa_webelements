from selenium import webdriver

firefox = webdriver.Firefox(executable_path="drivers/geckodriver")
firefox.implicitly_wait(10)
firefox.get("https://yandex.ru")

home_tabs = firefox.find_element_by_css_selector(".home-tabs3")
search_input = firefox.find_element_by_css_selector("input#text")

html = home_tabs.get_property("innerHTML")
# print(html)

attr = home_tabs.get_attribute("data-bem")
# print(attr)

css = home_tabs.value_of_css_property("margin-bottom")
# print(css)

firefox.close()

firefox.execute_script("alert('Hello!');")
