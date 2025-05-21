from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def browser():
    
    chrome_options = webdriver.ChromeOptions()
   

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
