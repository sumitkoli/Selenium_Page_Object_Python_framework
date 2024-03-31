import pytest
from selenium import webdriver

from utilities.ReadConfigurations import read_configurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = read_configurations("basic info", "browser")

    if browser.__eq__('chrome'):
        driver = webdriver.Chrome()
    elif browser.__eq__('firefox'):
        driver = webdriver.Firefox()
    elif browser.__eq__('edge'):
        driver = webdriver.Edge()
    else:
        print('Invalid driver name')

    driver.maximize_window()
    url = read_configurations("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
