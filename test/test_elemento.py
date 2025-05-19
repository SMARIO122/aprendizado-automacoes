from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_elemento_visivel(browser):
    url = "http://127.0.0.1:8050"
    browser.get(url)

    # Aguarda até que o <h1> com o texto 'Terminal Geek' esteja visível
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Terminal Geek']"))
    )

    elemento = browser.find_element(By.XPATH, "//h1[text()='Terminal Geek']")
    assert elemento is not None


