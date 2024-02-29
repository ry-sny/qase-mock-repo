import random

import pytest
from qaseio.pytest import qase

from selenium import webdriver


@pytest.fixture
def browser():
    url = "https://google.com"
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    logs = "\n".join(str(row) for row in driver.get_log('browser')).encode('utf-8')
    qase.attach((logs, "text/plain", "browser.log"))
    driver.quit()

def capture_screenshot(browser, name):
    qase.attach((browser.get_screenshot_as_png(), "image/png", name))

def test_screenshot(browser):
    browser.get("https://qase.io/login")
    capture_screenshot(browser, "test.png")
    assert False

def test_screenshot_2(browser):
    browser.get("https://qase.io/login")
    capture_screenshot(browser, "test2.png")
    assert False


def test_multiple_screenshots(browser):
    browser.get("https://google.com")
    capture_screenshot(browser, "google.png")
    browser.get("https://qase.io")
    capture_screenshot(browser, "qase.png")


def test_flaky_test():
    val = random.randrange(3)
    assert val == 1


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5])
def test_params(number):
    """
    mark can be used to apply "inline" parameterization, without a fixture
    """
    print("\nRunning test_numbers with {}".format(number))
    assert number % 2 == 0








