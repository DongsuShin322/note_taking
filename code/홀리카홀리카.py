from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
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

file_name = 'holikaholika.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.maximize_window()
driver.get("https://www.holikaholika.co.kr/FrontStore/PointBBS/iBoardList.phtml?bbsid=pbbs_store")
df = pd.DataFrame(columns=['name','addr','tel'])

while True:
    driver.find_element_by_css_selector('#contents > div.map_cell.j6-justify_.box.list > div.list.right > div.j6-paging_.ty2 > a.direction.next').click()
    time.sleep(3)
    try:
        Alert(driver).accept()
    except:
        time.sleep(1)
        pass
    else:
        time.sleep(1)
        last_page = int(driver.find_element_by_class_name('j6-paging_').find_elements_by_tag_name('a')[-2].text)
        break
        
driver.close()

base_url = 'https://www.holikaholika.co.kr/FrontStore/PointBBS/iBoardList.phtml?bbsid=pbbs_store&iCategory=0&_oSName=0&_oSSubject=0&_oSContents=0&_oSAddr=0&_oSearchText=&iPage={}'

for i in range(1, last_page+1):
	req = requests.get(base_url.format(i))
	html = req.content
	bs = BeautifulSoup(html, 'html.parser')
	stores = bs.find('ul', class_='ty_ul').find_all('li')
	for s in stores:
		name = s.find('dt').text
		addr = s.find('span', class_='address').text.split(':')[1].strip()
		tel = s.find('span', class_='tell').contents[1].text
		df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
	print ('{}-page done'.format(i))

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

