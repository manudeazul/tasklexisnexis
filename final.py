#Importando drivers necessários e abrindo o site no Chrome

from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://selenium-python.readthedocs.io/")

# procurando todos os elementos que tem a tag a e criando uma lista com eles
lis_links= navegador.find_elements_by_tag_name("a")

for link in lis_links:
    '''
    for que busca de uma a (link) dentro da lista de links que tenha "getting-started" o na referencia href
    quando ele acha, coloca o elmento que estamos procurando dentro da variavel elem e sai de dentro do for 
    '''
    if "getting-started" in link.get_attribute('href'):
        elem = link
        break

elem.click() #clica no elem
