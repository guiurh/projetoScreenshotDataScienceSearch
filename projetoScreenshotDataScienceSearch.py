from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = Firefox()
browser.get('https://google.com')
browser.maximize_window()

barraPesquisa = browser.find_element(By.XPATH, '//div//input[@title="Pesquisar"]')
barraPesquisa.send_keys("Google Acadêmico")
barraPesquisa.send_keys(Keys.ENTER)

sleep(3)

googleAcademico = browser.find_element(By.XPATH, '//div//a//h3["Google Acadêmico"]')
googleAcademico.click()

sleep(3)

pesquisaAcademico = browser.find_element(By.XPATH, '//div//input[@aria-label="Pesquisar"]')
pesquisaAcademico.click()
pesquisaAcademico.send_keys('Data Science')
pesquisaAcademico.send_keys(Keys.ENTER)

sleep(2)
browser.save_screenshot('path/nome.png')


#  Também pode ser utilizado da forma abaixo:

#browser.get_screenshot_as_file('path/nome.png')

