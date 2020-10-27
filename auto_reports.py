#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_driver=r"D:\ProgramData\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=chrome_driver)

def auto_report(username, password):
    url = "https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu"
    # chrome_options = Options()
    #
    # chrome_options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
    #
    # chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    #
    # chrome_options.add_argument('--no-sandbox') # 以最高权限运行

    print("opening windows...")
    driver = webdriver.Chrome(executable_path=chrome_driver)#options = chrome_options)
    driver.get(url)
    time.sleep(1)

    print("inputting id and password...")
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(1)

    # login
    driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
    print("logging successful...")
    time.sleep(3)

    # day health report
    print("enter day health report page...")
    driver.find_element_by_xpath('//*[@id="mainPage-page"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]').click()
    time.sleep(5)

    # all currently open windows
    windows = driver.window_handles
    # Switch to the latest open window
    driver.switch_to.window(windows[-1])
    time.sleep(1)

    # my form
    print("enter my form...")
    driver.find_element_by_xpath('//*[@id="mainM"]/div/div/div/div[1]/div[2]/div/div[3]/div[2]').click()
    time.sleep(3)

    promise_info = driver.find_element_by_xpath('//*[@id="select_1582538939790"]/div/div/span[1]').get_attribute('textContent')
    if 'Yes' in promise_info:
        print("reported, please don't report again!")
    else:
        # promise
        print("select Yes...")
        driver.find_element_by_xpath('//*[@id="select_1582538939790"]/div').click()
        time.sleep(2)

        # Yes
        driver.find_element_by_xpath('/html/body/div[8]/ul/div/div[3]/li').click()
        time.sleep(1)

        # save
        driver.find_element_by_xpath('//*//span[contains(@class, "form-save position-absolute")]').click()
        time.sleep(2)

        # accept
        driver.switch_to.alert.accept()
        print("saved successful!")

    # quit
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    username = [""]
    password = [""]
    for i in range(0,len(username)):
        try:
            auto_report(username[i], password[i])
            time.sleep(5)
        except Exception as e:
            print(e)
            exit(0)