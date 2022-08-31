import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://login.inbox.lv/signup?go=portal')


# iframe = driver.find_element_by_id("codefile_iframe")    
# driver.switch_to.frame(iframe)


first_names = ['Steve', 'Kamil', 'Camillo', 'Camilla', 'Tiger', 'Jason', 'Mario', 'Maru', 'Jack', 'Teremin', 'Wood', 'Hope', 'Kind', 'Kuba', 'Jakub', 'Adrian', 'Ada', 'Janina', 'Barbara', 'Michael', 'Ken']
last_names = ['Chander', 'Tander', 'Tender', 'Dunder', 'Duffer', 'Caulfield', 'Talo', 'Daru', 'Marone', 'Jackson', 'Smith', 'Scott', 'Carell', 'Levine']


first_name = random.choice(first_names)
last_name = random.choice(last_names)

number = random.randint(1, 1000)


# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='codefile_iframe']")))

wait = WebDriverWait(driver, 10)


first_name_input = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[1]/div[1]/div[2]/input')
first_name_input.send_keys(first_name)


last_name_input = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[1]/div[1]/div[3]/input')
last_name_input.send_keys(last_name)


username_input = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[1]/div[1]/div[1]/div/input')
username_input.send_keys(f'{first_name}.{last_name}{number}')


password_input = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[1]/div[1]/div[4]/div/input')
password_input.send_keys('Pilkal_100')


confirm_password = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[1]/div[1]/div[5]/div/input')
confirm_password.send_keys('Pilkal_100')


privacy_policy_checkbox = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[3]/div[1]/div[1]/label/input')
privacy_policy_checkbox.click()


time.sleep(1)


privacy_policy_accept_btn = driver.find_element('xpath', '/html/body/div[5]/div/div/div[3]/button[2]')
privacy_policy_accept_btn.click()

terms_of_service_btn = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[3]/div[1]/div[2]/label/input')
terms_of_service_btn.click()


finish_btn = driver.find_element('xpath', '/html/body/div[1]/article/div/div/div[2]/form/fieldset/div[3]/div[2]/button')
finish_btn.click()


count = 0


### automated CAPTCHA screenshots ###

def captcha_screenshot_machine():
    for i in range(1000): 
        count += 1
        time.sleep(1)
        

        captcha_screen = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div[1]')))
        captcha_screen.screenshot('/home/pexny/Pictures/Screenshots/CAPTCHA_' + str(count)+'.png')


        regenerate_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/button')))
        regenerate_btn.click()


# captcha_screenshot_machine()