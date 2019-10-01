from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from datetime import date

today = date.today()
year = today.year
month = today.month
day = today.day

save_file_name = str(year)+str(month)+str(day)
file_path = os.path.join(os.getcwd(), save_file_name)

file_name = 'missha.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get("http://www.beautynet.co.kr/customer/shop.list.do?brandNumber=1")

df = pd.DataFrame(columns=['name','addr','tel'])

cnt = 1
while True:
    print ('{}-page'.format(cnt))
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(0.2)
    stores = bs.find('table', {'summary':'매장명, 주소, 전화번호, 약도를 나타내는 미샤 매장 리스트'}).find('tbody').find_all('tr')
    for s in stores:
        name = s.find_all('td')[0].text.strip()
        addr = s.find_all('td')[1].text.strip()
        tel = s.find_all('td')[2].text.strip()
        df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    try:
        driver.find_element_by_css_selector('#rightSide > div.paging > div > a.nextBtn').click()
        time.sleep(3)
        cnt += 1
    except:
        break
        
driver.close()

new_df = df.drop_duplicates()
print ('original df :', len(df))
print ('drop_duplicated df :', len(new_df))
if len(df) == len(new_df):
    df.to_csv(save_path, encoding='cp949', index=False)
else:
    new_df.to_csv(save_path, encoding='cp949', index=False)
    ori_file_name = 'original_' + file_name
    ori_save_path = os.path.join(file_path, ori_file_name)
    df.to_csv(ori_save_path, encoding='cp949', index=False) 