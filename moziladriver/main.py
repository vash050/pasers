import time

from fake_useragent import UserAgent
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", UserAgent().random)

driver = webdriver.Firefox(
    executable_path='/home/vasiliy/my_prodject/parsers/moziladriver/geckodriver',
    options=options
)

# url = 'https://moidom.citylink.pro/pub/212'
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'


def main():
    try:
        driver.get(url=url)
        time.sleep(20)


    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
