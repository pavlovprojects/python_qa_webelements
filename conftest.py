import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    # driver.get("https://konflic.github.io/some_app/index.html")
    return driver
