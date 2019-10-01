import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import date

today = date.today()
year = today.year
month = today.month
day = today.day

save_file_name = str(year)+str(month)+str(day)
file_path = os.path.join(os.getcwd(), save_file_name)

file_name = 'toocoolforschool.csv'
save_path = os.path.join(file_path, file_name)
df = pd.DataFrame(columns=['name','addr','tel'])

url = 'http://www.toocoolforschool.com/shop/shopinfo/shopinfo.php'

req = requests.get(url)
html = req.content
bs = BeautifulSoup(html, 'html.parser')

last_page = int(bs.find('div', class_='paging').find_all('a')[-1].attrs['href'].split('page=')[1])

base_url = 'http://www.toocoolforschool.com/shop/shopinfo/shopinfo.php?&page={}'

for i in range(1, last_page+1):
    req = requests.get(base_url.format(i))
    html = req.content
    bs = BeautifulSoup(html, 'html.parser')
    stores = bs.find('div', class_='board-list').find('tbody').find_all('tr')
    for s in stores:
    	name = s.find_all('div', class_='td_wrap')[0].text
    	addr = s.find('div', class_='sbj').text
    	tel = s.find_all('div', class_='td_wrap')[1].text
    	df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)

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
