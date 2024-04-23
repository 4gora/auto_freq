from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

from info import user, pw

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://univirtus.uninter.com/ava/web/#/")

driver.find_element("xpath", '//*[@id="ru"]').send_keys(user)
driver.find_element("xpath", '//*[@id="senha"]').send_keys(pw)
driver.find_element("xpath", '//*[@id="loginBtn"]').click()
sleep(2)
driver.find_element("xpath", '//*[@id="loginBoxAva"]/i').click()
sleep(3)
driver.find_element("xpath", '//*[@id="escola_9"]').click()
sleep(1)
driver.find_element(
    "xpath",
    "//span[.='TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - TELEPRESENCIAL - EAD']",
).click()
sleep(1)
reference = '//span[text()="Fundamentos de Design de Sistemas"]'
elemento_span = driver.find_element('xpath', reference)
elemento_a = elemento_span.find_element('xpath', 'ancestor::a')
elemento_a.click()
driver.find_element('xpath', reference).click()
sleep(1)
driver.find_element(
    "xpath",
    "//span[.='Frequência']",
).click()
input()
