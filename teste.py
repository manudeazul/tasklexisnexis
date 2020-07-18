from selenium import webdriver
from selenium.webdriver import Chrome

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

#assert "No results found." not in navegador.page_source
