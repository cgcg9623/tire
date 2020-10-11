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

# tr 갯수만큼 for를 돌려 사이즈별 spec을 뽑는다
for tire_spec in tires_spec:
    for i in range(1, j-1) :
        prod_size = tire_spec.select_one(f'tr:nth-child({i}) > td.size > a:nth-child(1) > span')
        prod_UTQG = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(2) > a')
        prod_MaxLoad = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(3)')
        prod_MaxInflationPressure = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(4)')
        prod_TreadDepth = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(5)')
        prod_TireWeight = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(6)')
        prod_RimWidthRange = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(7)')
        prod_MeasuredRimWidth = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(8)')
        prod_SectionWidth = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(9)')
        prod_TreadWidth = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(10)')
        prod_OverallDiameter = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(11)')
        prod_CountryOfOrigin = tire_spec.select_one(f'tr:nth-child({i}) > td:nth-child(13) > a > div > div.ui-tooltip-content > b')

        # 값이 없을때가 있음
        if prod_size.text == None :
            print("사이즈 : ", "N/A")
        else :
            print("사이즈 : ", prod_size.text)
        if prod_UTQG.text == None :
            print("UTQG : ", "N/A")
        else :
            print("UTQG : ", prod_UTQG.text)
        if prod_MaxLoad.text == None :
            print("Max Load : ", "N/A")
        else :
            print("Max Load : ", prod_MaxLoad.text)
        if prod_MaxInflationPressure.text == None :
            print("Max Inflation Pressure : ", "N/A")
        else :
            print("Max Inflation Pressure : ", prod_MaxInflationPressure.text)
        if prod_TreadDepth.text == None :
            print("Tread Depth : ", "N/A")
        else :
            print("Tread Depth : ", prod_TreadDepth.text)
        if prod_TireWeight.text == None :
            print("Tire Weight : ", "N/A")
        else :
            print("Tire Weight : ", prod_TireWeight.text)
        if prod_RimWidthRange.text == None :
            print("Rim Width Range : ", "N/A")
        else :
            print("Rim Width Range : ", prod_RimWidthRange.text)
        if prod_MeasuredRimWidth.text == None :
            print("Measured Rim Width : ", "N/A")
        else :
            print("Measured Rim Width : ", prod_MeasuredRimWidth.text)
        if prod_SectionWidth.text == None :
            print("Section Width : ", "N/A")
        else :
            print("Section Width : ", prod_SectionWidth.text)
        if prod_TreadWidth.text == None :
            print("Tread Width : ", "N/A")
        else :
            print("Tread Width : ", prod_TreadWidth.text)
        if prod_OverallDiameter.text == None :
            print("Overall Diameter : ", "N/A")
        else :
            print("Overall Diameter : ", prod_OverallDiameter.text)
        if prod_CountryOfOrigin.text == None :
            print("Country Of Origin : ", "N/A")
        else :
            print("Country Of Origin : ", prod_CountryOfOrigin.text)


driver.quit()
#wb.save(filename='articles.xlsx')