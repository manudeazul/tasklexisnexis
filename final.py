#Importando drivers necessários e abrindo o site no Chrome

from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://selenium-python.readthedocs.io/")

def letrasRepetidas (letra0, texto):
    '''
    Função recursiva que tem como paremetro a primeira letra de uma frase e o resto da frase
    Com isso ela verifica se o texto é apenas uma letra (porque nesse caso só tem uma comparação) ou se é maior.
    Se for maior
        verifica se aquela letra existe no texto
        se existe retorna True, senão retorna a função com a proxima letra e o resto do texto
    Se não for maior, compara com a letra com o texto. Se são iguais retorna True, senão False
    '''
    if len(texto) > 1:
        if letra0 in texto:
            return True
        else:
            return letrasRepetidas(texto[0],texto[1:])
    else:
        if letra0 in texto:
            return True
        else:
            return False


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

assert "2. Getting Started — Selenium Python Bindings 2 documentation" in navegador.title # conferindo se estamos na página desejada

texto_corpo = navegador.find_element_by_class_name('body').text #pegando o texto do site que se encontra no elemento com a classe body
busca = "Getting Started" #esse é o elemento que estamos buscando

'''
verificando se o texto que estamos procurando se encontr no corpo da página que queremos
se achar vai aparecer no console que foi achado, senão vai aparecer também
'''
if busca in texto_corpo:
    print('Texto achado')
else:
    print('Texto não achado')


'''
vendo se a função que criei para conferir se tem letrar repetidas retorna True
se for True vai aparecer no console que tem letras repetidas, senão vai aparecer também
'''
if letrasRepetidas(busca[0],busca[1:]):
    print('Tem Letras Repetidas')
else:
    print('Não tem Letras Repetidas')
