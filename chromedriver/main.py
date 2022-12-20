import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent= {UserAgent().random}')

driver = webdriver.Chrome(
    executable_path='/home/vasiliy/my_prodject/parsers/chromedriver/chromedriver',
    options=options
)

url = 'https://moidom.citylink.pro/pub/212'
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'


def main():
    try:
        driver.get(url=url)

        button_save_late = driver.find_element(By.CLASS_NAME, "btn-save-later")
        print(button_save_late.text)
        button_save_late.click()

        time.sleep(10)
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
