import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent= {UserAgent().random}')
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_argument('window-size=2560,1440')

driver = webdriver.Chrome(
    executable_path='/home/vasiliy/my_prodject/parsers/chromedriver/chromedriver',
    options=options
)

url = 'https://moidom.citylink.pro/pub/212'


# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'


def main():
    try:
        driver.get(url=url)
        time.sleep(2)

        button_save_late = driver.find_element(By.CLASS_NAME, "btn-save-later")
        button_save_late.click()

        play = driver.find_element(By.CLASS_NAME, 'vjs-big-play-button')

        play.click()

        full_screen = driver.find_element(By.CLASS_NAME, "vjs-fullscreen-control")
        full_screen.click()



        time.sleep(360000)

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
