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

file_name = 'naturerepublic.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get("http://brand.naturerepublic.com/brand/store")
df = pd.DataFrame(columns=['name','addr','tel'])

# 지역검색
driver.find_element_by_xpath("""//*[@id="map_area"]/dl/dd[1]/ul/li[2]/a""").click()
time.sleep(0.2)

sido = driver.find_element_by_xpath("""//*[@id="div_region_srch"]/div[1]/div/ul""")
num_sido = len(sido.find_elements_by_tag_name('li'))
for i in range(1, num_sido):
    # 전체 시도 select box
    driver.find_element_by_xpath("""//*[@id="div_region_srch"]/div[1]/div""").click()
    time.sleep(1)
    sido = driver.find_element_by_xpath("""//*[@id="div_region_srch"]/div[1]/div/ul""")
    # 특정 시도 선택
    sido.find_elements_by_tag_name('li')[i].click()
    time.sleep(1)
    gugun = driver.find_element_by_xpath("""//*[@id="div_region_srch"]/div[2]/div/ul""")
    num_gugun = len(gugun.find_elements_by_tag_name('li'))
    for j in range(num_gugun):
        # 전체 군구 select box
        driver.find_element_by_xpath("""//*[@id="div_region_srch"]/div[2]/div""").click()
        time.sleep(1)
        gugun = driver.find_element_by_xpath("""//*[@id="div_region_srch"]/div[2]/div/ul""")
        # 특정 군구 선택
        gugun.find_elements_by_tag_name('li')[j].click()
        time.sleep(1)
        # 검색
        driver.find_element_by_xpath("""//*[@id="div_region_srch"]/a""").click()
        time.sleep(1)
        bs = BeautifulSoup(driver.page_source, 'html.parser')
        time.sleep(1)
        stores = bs.find('ul', {'id':'ul_store_list'}).find_all('li')
        for s in stores:
            name = s.find('dt').text.replace('\n','').replace('\t','').strip()
            addr = s.find('dd', class_='address').text.replace('\n','').replace('\t','').strip()
            tel = s.find('dd', class_='phone').text.replace('\n','').replace('\t','').strip()
            df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    time.sleep(5)

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