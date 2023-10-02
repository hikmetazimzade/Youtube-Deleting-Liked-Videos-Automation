import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

import time
import keyboard

gmail = input("Input your gmail:")
password = input("Input you password:")

while True:
    try:
        starting_point = int(input("Input the number of video you want to start deleting with:"))
        last_point = int(input("Input the number of video you want to delete until:"))
        break
    except:
        pass

if __name__ == "__main__":
    driver = uc.Chrome(use_subprocess = True)
    driver.maximize_window()
    driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Daz%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=az&ifkv=AYZoVheJfp-zjzvwrX8ciV29JOByMriEcdqX9wkNlLkmwdUsAnt4xdmRp0HSk6v3Oyq7_EWd2X8n&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-805179657%3A1694338753237137&theme=glif")


    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//input[@type="email"]'))).send_keys(gmail, Keys.ENTER)
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(password, Keys.ENTER)
    driver.implicitly_wait(15)
    time.sleep(3)
    keyboard.press_and_release("Esc")

    try:
        elements = driver.find_elements(By.XPATH, '//*[@class="style-scope ytd-guide-collapsible-section-entry-renderer"]')
        elements[7].click()

    except:
        driver.get("https://www.youtube.com/")
        driver.implicitly_wait(10)
        elements = driver.find_elements(By.XPATH, '//*[@class="style-scope ytd-guide-collapsible-section-entry-renderer"]')
    elements[7].click()

    driver.implicitly_wait(10)
    time.sleep(3)
    keyboard.press_and_release("Esc")
    video_number = driver.find_element(By.XPATH,'//*[@id="page-manager"]/ytd-browse[2]/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]/span[1]').text
    video_number = video_number.replace(',', '')

    if int(video_number) < starting_point:
        print('There are not enough videos!')
        driver.close()


    if last_point > 100:
        current_height = 10000
        loop_number = last_point // 100

        for i in range(loop_number):
            driver.execute_script(f'window.scrollBy(0,{current_height})', "")
            current_height += 10000
            time.sleep(3)


    buttons = driver.find_elements(By.CSS_SELECTOR, '#button > yt-icon > yt-icon-shape > icon-shape > div')
    starting_point += 7
    last_point += 7
    if last_point > len(buttons) : last_point = len(buttons)


    action = ActionChains(driver)
    action.move_to_element(buttons[starting_point]).perform()
    time.sleep(3)
    
    for i in range(starting_point, last_point):#The last point is not included
        buttons[i].click()
        driver.find_element(By.XPATH, '//*[@id="items"]/ytd-menu-service-item-renderer[5]/tp-yt-paper-item').click()
        time.sleep(0.5)

    print("Videos Deleted Successfully!")
    driver.close()
