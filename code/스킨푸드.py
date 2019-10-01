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

file_name = 'skinfood.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get("http://www.theskinfood.com/m/brand/brandFindShop.do")

df = pd.DataFrame(columns=['name','addr','tel'])

sido = driver.find_element_by_css_selector('#cr > div > div.container > div > div.container > div > div.box.mg-btm15 > div.mg-btm15.option-wrap > div.float-left.selBox')
sido.click()
time.sleep(2)
sido.find_element_by_class_name('heapOption').click()
time.sleep(2)

while True:
	try:
		driver.find_element_by_css_selector('#cr > div > div.container > div > div.container > div > div.more-wrap.mg-btm30 > a').click()
		time.sleep(3)
	except:
		bs = BeautifulSoup(driver.page_source, 'html.parser')
		time.sleep(0.2)
		driver.close()
		stores = bs.find('ul', {'id':'storeListDiv'}).find_all('li')
		for s in stores:
			name = s.find('strong').text
			addr = s.find_all('p')[0].text
			tel = s.find_all('p')[1].text
			df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
		break

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