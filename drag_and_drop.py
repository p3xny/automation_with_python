from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # This line import multiple action chains that can be performed, like .drag_and_drop() 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element('xpath', '//*[@id="box1"]')
destination = driver.find_element('xpath', '//*[@id="box101"]')

actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()



