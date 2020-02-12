import pytest
from selenium import webdriver

CHROMEDRIVER = "../../Env/drivers/chromedriver"
GECKODRIVER = "../../Env/drivers/geckodriver"


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://demo.opencart.com/", help="choose your browser")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    elif browser_param == "firefox":
        driver = webdriver.Firefox(executable_path=GECKODRIVER)
    elif browser_param == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(10)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))

    return driver
