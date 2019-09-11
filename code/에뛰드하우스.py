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

file_name = 'etudehouse.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get("https://www.etudehouse.com/kr/ko/display/store_location?displayMenuId=store_location")

df = pd.DataFrame(columns=['name','addr','tel'])

cnt = 1
while True:
    print ('{}-page'.format(cnt))
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    stores = bs.find_all('div', class_='store_item')
    for s in stores:
        name = s.find('h3', class_='store_title').text
        addr = s.find('p', class_='store_addr').contents[0].replace('\n','').replace('\t','')
        tel = s.find('p', class_='store_addr').contents[1].text.replace('\n','').replace('\t','')
        df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    
    next_button = driver.find_element_by_css_selector('#ap_container > div.ap_contents.brand > div > div > div.tab_cont.pd0.store_find_area > div > div.store_right_wrap > div.pagination.＠paging-apply > a.navi.next')
    
    if next_button.get_attribute('disabled') == None:
    	next_button.click()
    	time.sleep(3)
    	cnt += 1
    else:
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