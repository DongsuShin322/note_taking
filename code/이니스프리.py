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

file_name = 'innisfree.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get('http://www.innisfree.com/kr/ko/FindStoreList.do')

def save(df):
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(0.2)
    stores = bs.find('table', {'summary':'매장명, 주소, 전화번호, 위치로 구성된 지역별 매장 목록'}).find('tbody').find_all('tr')
    for s in stores:
        name = s.find_all('td')[0].text.replace('\xa0', ' ').strip()
        addr = s.find_all('td')[1].text.replace('\xa0', ' ').strip()
        tel = s.find_all('td')[2].text.replace('\xa0', ' ').strip()
        df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    return df

driver.find_element_by_xpath("""//*[@id="findShopTab"]""").click()
time.sleep(3)

df = pd.DataFrame(columns=['name','addr','tel'])

cnt = 0
while True:
    cnt += 1
    print ('{}-page'.format(cnt))
    df = save(df)
    pages = driver.find_elements_by_class_name("num")
    num_page = len(pages) 
    for i in range(1, len(pages)):
        p = driver.find_elements_by_class_name("num")
        p[i].click()
        time.sleep(5)
        cnt += 1
        print ('{}-page'.format(cnt))
        df = save(df)
    try:
        driver.find_element_by_class_name("next").click()
    except:
        break
    else:
        time.sleep(5)
        continue
        
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