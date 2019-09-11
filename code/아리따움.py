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

file_name = 'aritaum.csv'
save_path = os.path.join(file_path, file_name)

driver = webdriver.Chrome('C:/Users/ds.sin/Desktop/Python/crawling/chromedriver')
driver.get("https://www.aritaum.com/promotion/st/promotion_st_store_find.do")
df = pd.DataFrame(columns=['name','addr','tel'])

driver.find_element_by_xpath("""//*[@id="li_region_search"]""").click()
time.sleep(1)
sido = driver.find_element_by_xpath("""//*[@id="region_search"]/div/span[1]""")
num_sido = len(sido.find_elements_by_tag_name('li'))
for i in range(1, num_sido):
    sido = driver.find_element_by_xpath("""//*[@id="region_search"]/div/span[1]""")
    sido.click()
    time.sleep(1)
    sido.find_elements_by_tag_name('li')[i].click()
    time.sleep(1)
    gugun = driver.find_element_by_xpath("""//*[@id="region_search"]/div/span[2]""")
    num_gugun = len(gugun.find_elements_by_tag_name('li'))
    for j in range(1, num_gugun):
        gugun = driver.find_element_by_xpath("""//*[@id="region_search"]/div/span[2]""")
        gugun.click()
        time.sleep(1)
        gugun.find_elements_by_tag_name('li')[j].click()
        time.sleep(1)
        driver.find_element_by_xpath("""//*[@id="region_search"]/div/span[3]""").click()
        time.sleep(1)
        bs = BeautifulSoup(driver.page_source, 'html.parser')
        stores = bs.find('ul', class_='scrollArea').find_all('li')
        for s in stores:
            name = s.find('p', class_='name').text
            addr = s.find('p', class_='address').text
            tel = s.find('p', class_='tel').text
            df = df.append({'name':name, 'addr':addr, 'tel':tel}, ignore_index=True)
    time.sleep(3)

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