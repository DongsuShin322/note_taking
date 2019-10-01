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

file_name = 'naturecollection.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get("http://naturecollection.co.kr/naturecollection/store/search.jsp")
df = pd.DataFrame(columns=['name','addr','tel'])
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(0.3)
    stores = bs.find('tbody', {'id':'storeResultListTbody'}).find_all('tr')
    for s in stores:
        name = s.find_all('td')[0].text
        addr = s.find_all('td')[1].text
        tel = s.find_all('td')[2].text
        df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    try:
        driver.find_element_by_css_selector('#more > a:nth-child(13)').click()
        time.sleep(2)
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