from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook


driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

articles = soup.select('#widget-grid > div > div.col-sm-12.col-md-12.col-lg-12.ng-scope > div > div:nth-child(1) > div.col-md-8.col-sm-9.col-xs-12 > div:nth-child(1) > div.col-sm-12.col-md-8.col-lg-8 > div.ws-element-name > h1')
for article in articles:
    prod_name = article.select_one('div:nth-child(1) > div.col-sm-12.col-md-8.col-lg-8 > div.ws-element-name > h1').text
    url = article.select_one('dl > dt > a')['href']
    corp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    img = article.select_one('div > a > img')['src']
    ws1.append([title, url, corp, img])

    print(title, url, corp, img)



driver.quit()
wb.save(filename='articles.xlsx')