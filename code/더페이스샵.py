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

file_name = 'thefaceshop.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get("http://www.thefaceshop.com/brand/store/list.jsp")

df = pd.DataFrame(columns=['name','addr','tel'])

def save(df):
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(0.2)
    stores = bs.find('table', class_="tbl_type5").find('tbody').find_all('tr')[:-1]
    for s in stores:
        name = s.find_all('td')[0].text
        tel = s.find_all('td')[1].text
        addr = s.find_all('td')[2].text
        df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    return df

cnt = 1
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:
    print ('{}-page'.format(cnt))
    df = save(df)
    driver.find_elements_by_class_name('prev')[-1].click()
    cnt += 1
    time.sleep(2)
    if driver.find_elements_by_class_name('prev')[0] == driver.find_elements_by_class_name('prev')[-1]:
        print ('{}-page'.format(cnt))
        df = save(df)
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