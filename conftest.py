from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def browser():
    chrome_path = "/home/smario122/dash/chrome-linux64/chrome"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--user-data-dir=/tmp/test-profile")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
