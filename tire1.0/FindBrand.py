from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

url = "https://www.tirerack.com/content/tirerack/desktop/en/tires/by-brand.html"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# 브랜드 리스트 생성
brand_list = []
# 브랜드 불러오기
tires_info = soup.select('#ui-brandListBlog > div > ul > a')
for tire_info in tires_info:
    brand_name = tire_info.select_one('li > div > img')['title']

    print("브랜드명 : ", brand_name)
    brand_list.append(brand_name)

    #url = article.select_one('dl > dt > a')['href']
    #corp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    #img = article.select_one('div > a > img')['src']
    #ws1.append([title, url, corp, img])
print(brand_list)

driver.quit()
#wb.save(filename='articles.xlsx')