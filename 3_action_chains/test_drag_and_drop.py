from selenium.webdriver import ActionChains


def test_d_and_d(browser):
    browser.get("https://konflic.github.io/front_example/draganddrop.html")
    browser.maximize_window()

    # Итерируемся по 10 элементам которые нужно перебросить
    for i in range(1, 11):
        # Создаю объект для действия
        action = ActionChains(browser)

        # Создаю строки для селекторов
        card_id = "card{}".format(i)
        zone_id = "zone{}".format(i)

        # Нахожу нужные элементы
        card_element = browser.find_element_by_id(card_id)
        zone_element = browser.find_element_by_id(zone_id)

        # Создаю действие
        action.click_and_hold(card_element).pause(0.5).move_to_element(zone_element).release()

        # Выполняю действие
        action.perform()