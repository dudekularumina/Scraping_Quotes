from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome()

def Commonfields():
    quote={
        'quotes':[],
        'quote_by':[],
        'about_author':[]
    }
    return(quote)


# url=["http://quotes.toscrape.com/page/{a}/"]

def quotes_scraping(Commonfields):
    quote=Commonfields
    for a in range(1,11):
        url="http://quotes.toscrape.com/page/{}/".format(a)
        driver.get(url)
        # url=(url).format(a=a)

        print("Page URL+++++++++++++++++++", url)

        time.sleep(2)
        html_content=driver.page_source
        soup=BeautifulSoup(html_content, 'html.parser')

        all_quotes=soup.find_all("div", class_='quote')
        print("Length of Quotes----------------------", len(all_quotes))
        for q in all_quotes:
            quotess=q.find("span", class_="text").text.strip()
            # print("Quotes-----------------", quotess)

            author=q.find("small", class_='author').text.strip()
            # print("Author------------------",author)

            about_author=q.find('a')['href']
            # print("About Author....", about_author)
            about_author="https://quotes.toscrape.com"+about_author
            # print("About Author--------------", about_author)

          
            quote['quotes'].append(quotess)
            quote['quote_by'].append(author)
            quote['about_author'].append(about_author)

    return quote

import pandas as pd
            # print("Quotes+++++++++++++++++++++++++++++++++++++=",quote)





# Commonfields()
quotes_dict=quotes_scraping(Commonfields())
df=pd.DataFrame(quotes_dict)

print("Data Frame...................")
print(df)

#To CSV Fille
df.to_csv('quotes.csv', index=False)


#To Excel 
df.to_excel('quotes.xlsx', engine='openpyxl')






