# coding: utf-8


from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/welcome')
    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm1.click()
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(
        'zhongcuizhen@163.com')
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('uiop7890')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

except Exception as e:
    print(e)

finally:
    browser.close()






