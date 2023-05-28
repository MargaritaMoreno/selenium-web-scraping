import pandas as pd
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/usr/bin/chromedriver"
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)

url_audio = "https://www.audible.com/search?crid=DPBVM163HY6W&i=na-audible-us&k=horror&keywords=horror&node=18580628011&ref-override=a_search_t1_header_search&sprefix=fiction%2Cna-audible-us%2C156&url=search-alias%3Dna-audible-us&ref=a_search_l1_subcatRefs_1&pf_rd_p=daf0f1c8-2865-4989-87fb-15115ba5a6d2&pf_rd_r=QGNNWAW17ZW5PHTPS8JV&pageLoadId=KImmu33Y5SDzhzIn&creativeId=9648f6bf-4f29-4fb4-9489-33163c0bb63e"
driver.get(url=url_audio)

name = []
audio_title = driver.find_elements(By.CSS_SELECTOR, ".bc-list-item h3")
for title in audio_title:
    story_title = (title.text)
    if story_title != "":
        name.append(story_title)

amount = []
audio_price = driver.find_elements(By.CSS_SELECTOR, f".buybox-regular-price span")
for price in audio_price:
    regular_price = price.text
    if regular_price != "Regular price:":
        amount.append(regular_price)

cleaned_pricelist = [item for item in amount if item != '']
  

ratings =  []       
star_review = driver.find_elements(By.CSS_SELECTOR, "li .bc-pub-offscreen")
for star in star_review:
   estrella = star.text
   ratings.append(estrella)
del ratings [-2:]
cleaned_ratings = [item for item in ratings if item != '']

time.sleep(10)
driver.quit

data = {
    "Audiobook title": name,
    "Regular price": cleaned_pricelist,
    "Star rating": cleaned_ratings
}

df = pd.DataFrame(data)

df.to_csv("audible.csv", index=False)
