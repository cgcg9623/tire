from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%8A%AC%EA%B8%B0")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

i=1

thumbnails = soup.select("#imgList > div > a > img")
for thumbnail in thumbnails:
    dload.save(thumbnail['src'], f'img_homework/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기