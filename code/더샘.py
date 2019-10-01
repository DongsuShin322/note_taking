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

file_name = 'thesaem.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.maximize_window()
driver.get("http://www.thesaemcosmetic.com/page/cscenter/store/local")

df = pd.DataFrame(columns=['name','addr','tel'])

cnt = 0
while True:
    pages = driver.find_element_by_class_name('pagination').find_elements_by_tag_name('li')
    for i in range(len(pages)):
        if pages[i].get_attribute('class') == 'active':
            print ('{}-page'.format(i+cnt))
            break
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(0.2)
    stores = bs.find('tbody', {'id':'retailList'}).find_all('tr', class_='list_title')
    for s in stores:
        name = s.find('h4').text.replace('\n','').strip()
        addr = s.find('span', class_='address').text
        tel = s.find('span', class_='num').text
        df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    try:
        pages[i+1].click()
        time.sleep(5)
        cnt += 10
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