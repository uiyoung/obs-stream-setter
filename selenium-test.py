from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import pyautogui
import pyperclip
import ObsStreamSetter


def chromeWebdriver():
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')

    driver = webdriver.Chrome(service=chrome_service, options=options)

    return driver


driver = chromeWebdriver()
driver.get("https://auth.band.us/login_page")
# driver.maximize_window()

print(driver.current_url)  # http://www.google.com/

driver.implicitly_wait(10)


time.sleep(1)
nav = driver.find_element(By.PARTIAL_LINK_TEXT, '네이버')
nav.click()

# id = driver.find_element(By.ID, "id_line")
# id.click()
# pyperclip.copy("네이버아이디")
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(2)

# pw = driver.find_element(By.ID, 'pw_line')
# pw.click()
# pyperclip.copy("네이버비밀번호")
# pyautogui.hotkey('ctrl', 'v')

# time.sleep(1)
# loginBtn = driver.find_element(By.CLASS_NAME, 'btn_login')
# loginBtn.click()

# 로그인 될 때까지 대기
input("press any key after login")

driver.implicitly_wait(10)
driver.get('https://band.us/band/83393079/create-live')


# driver.implicitly_wait(10)
# driver.execute_script('window.open("https://band.us/band/83393079/create-live");')

# driver.implicitly_wait(10)
# driver.switch_to(driver.window_handles[1])


driver.implicitly_wait(10)
input('ready to generate keys?')

# only for ther first time
# closeBtn = driver.find_element(By.CLASS_NAME, 'btnLyClose')
# closeBtn.click()

title = driver.find_element(By.CLASS_NAME, 'liveIntroTextArea')
title.click()
title.send_keys('방송제목적기')

issueBtn = driver.find_element(By.CLASS_NAME, 'btnKeyIssue')
issueBtn.click()

driver.implicitly_wait(10)
time.sleep(1)

stream_url_copy_btn = driver.find_element(By.CLASS_NAME, '_btnCopyStreamUrl')
stream_url_copy_btn.click()
driver.implicitly_wait(1)
pyautogui.press('enter')
stream_url = pyperclip.paste()

stream_key_copy_btn = driver.find_element(By.CLASS_NAME, '_btnCopyStreamKey')
stream_key_copy_btn.click()
driver.implicitly_wait(1)
pyautogui.press('enter')
stream_key = pyperclip.paste()

print("url, key", stream_url, stream_key)
ObsStreamSetter.setStream(stream_url, stream_key)

while True:
    pass


# # driver.quit()

# while True:
#     pass
