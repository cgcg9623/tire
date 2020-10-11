from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook


driver = webdriver.Chrome('chromedriver')

url = "https://www.tirerack.com/tires/tires.jsp?tireMake=Pirelli&tireModel=P+Zero+Nero"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# 엑셀 만드는부분
# wb = Workbook()
# ws1 = wb.active
# ws1.title = "tires"
# ws1.append(["제목", "링크", "신문사", "썸네일"])

# 타이어 기본정보(브랜드, 제품명)
tires_info = soup.select('#product-details > div.product-details.right')
for tire_info in tires_info:
    brand = tire_info.select_one('div.brand-logo.fullW.left > meta')['content']
    prod_name = tire_info.select_one('h1').text

    print("브랜드명 : ", brand)
    print("제품명 : ", prod_name)

    #url = article.select_one('dl > dt > a')['href']
    #corp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    #img = article.select_one('div > a > img')['src']
    #ws1.append([title, url, corp, img])

# 타이어 스펙정보 찾기(사이즈 등)
tires_spec = soup.select('#allSpecs > div:nth-child(3) > table.specification.floatHead > tbody')

#tr 갯수 찾기(table row 갯수)
j = 0
for tag in soup.find_all('tr'):
    j += 1
print ("총 사이즈(열) 갯수 : ", j-2)