from lib2to3.pgen2 import driver
from telnetlib import EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import timeout
from bs4 import BeautifulSoup
import time

opts = Options() ## Read about Options
browser = Firefox(options=opts) ## Instantiating Firefox brwoser
browser.get('https://www.semrush.com/login')

inputEmail = browser.find_element_by_name("email").send_keys("vinniseng@gmail.com")
inputPassword = browser.find_element_by_name("password").send_keys("test1234")
loginButton = browser.find_element_by_xpath("//button[@data-test='login-page__btn-login']").click() ## XPath to locate login button

time.sleep(20)
search_form = browser.find_element_by_name("q")
search_form.send_keys('firstcry.com')
search_form.submit()

result = []
while True:
    time.sleep(15)
    result = browser.find_elements_by_id('domain-overview-app')
    time.sleep(10)
    
    print result[0].find_elements_by_xpath("//div[@class = 'style.module__mainNumber___pseVS']//a//span")[0].text
    # if len(result) != 0:
    #     soup = BeautifulSoup(result[0].get_attribute('innerHTML'), 'html.parser')
    #     row2Ele = soup.find('div', attrs={'class': 'summary.module__mainNumber___pseVS'})
    #     import pdb;pdb.set_trace()
    #     print(row2Ele)
    browser.close()
    #     break;

# search_form=''
# while not search_form:
#     try:
#         search_form = browser.find_element_by_class_name("tn-search-bar__input")
#         search_form.send_keys('firstcry.com')
#         search_form.submit()
#     except:continue

# browser.close()
# quit()

# delay = 10
# try:
#     search_form = WebDriverWait(browser, delay).until(staleness_of(By.CLASS_NAME, 'tn-search-bar__input'))
#     print("Page is ready!")
#
#     # search_form = browser.find_element_by_class_name("tn-search-bar__input")
#     search_form.send_keys('firstcry.com')
#     search_form.submit()
#
#     result = browser.find_elements_by_id('domain-overview-app')
#     print(result)
# except TimeoutException:
#     print("Loading took too much time!")
# finally:
#     browser.close()
#     quit()