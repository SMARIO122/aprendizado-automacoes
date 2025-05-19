from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_formulario_geek(browser):
    url = "http://127.0.0.1:8050"
    browser.get(url)

    campo = browser.find_element(By.ID, "campo-comando")
    botao = browser.find_element(By.ID, "botao-executar")

    campo.send_keys("ls -la")
    botao.click()

    # Dá um tempo pra resposta aparecer
    sleep(2)

    saida = browser.find_element(By.ID, "saida-terminal")
    assert "ls -la" in saida.text
    print("✅ Formulário preenchido e resposta validada com sucesso!")
