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

file_name = 'itsskin.csv'
save_path = os.path.join(file_path, file_name)

req = requests.get('https://www.itsskin.com/board/list.php?bdId=store&ftSearchStore=')
html = req.content
bs = BeautifulSoup(html, 'html.parser')

df = pd.DataFrame(columns=['name','addr','tel'])

stores = bs.find('ul', {'id':'storeList'}).find_all('li')

for s in stores:
    info = s.find('p', class_='title').contents
    name = info[0]
    if len(info) == 1:
        tel = ''
    else:
        tel = info[2]
    addr = s.find('p', class_='cont').text
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