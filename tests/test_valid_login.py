from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed(), "O login deu errado!"

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
assert driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack' and text()='Remove']").is_displayed(), "Produto não adicionado!"

driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
assert driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bolt-t-shirt' and text()='Remove']").is_displayed(), "Produto não adicionado!"

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed(), "Produto ausente no carrinho!"
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").is_displayed(), "Produto ausente no carrinho!"

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("João")
driver.find_element(By.ID, "last-name").send_keys("Carvalho")
driver.find_element(By.ID, "postal-code").send_keys("01234-567")

driver.find_element(By.ID, "continue").click()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed(), "Produto ausente no carrinho!"
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").is_displayed(), "Produto ausente no carrinho!"

driver.find_element(By.ID, "finish").click()
assert driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']").is_displayed(), "Não realizou a compra!"
