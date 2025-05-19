from selenium.webdriver.common.by import By

def test_botao_ok_visivel(browser):
    url = "http://127.0.0.1:8050"
    browser.get(url)

    # Verifica botão pelo ID
    botao = browser.find_element(By.ID, "botao-executar")

    assert botao.is_displayed()
    print("✅ Botão 'OK' visível na tela.")
