from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

def letrasRepetidas (letra0, texto):
    if len(texto) > 1:
        if letra0 in texto:
            return True, letra0
        else:
            return letrasRepetidas(texto[0],texto[1:])
    else:
        if letra0 in texto:
            return True, letra0
        else:
            return False



navegador = webdriver.Chrome()

navegador.get("https://selenium-python.readthedocs.io/")

#elem = navegador.find_element_by_name("q")
#elem.clear()
#elem.send_keys("Getting Started")
#elem.send_keys(Keys.RETURN)

lis_links= navegador.find_elements_by_tag_name("a")

for link in lis_links:
    if "getting-started" in link.get_attribute('href'):
        elem = link
        break

elem.click()

assert "2. Getting Started — Selenium Python Bindings 2 documentation" in navegador.title

texto_corpo = navegador.find_element_by_class_name('body').text
busca = "Eu gosto muito de picles"

if busca in texto_corpo:
    print('Texto achado')
else:
    print('Texto não achado')

if letrasRepetidas(busca[0],busca[1:]):
    print('Tem Letras Repetidas')
else:
    print('Não tem Letras Repetidas')
