#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:53:14 2019

@author: siyuanch
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

"A function that gets details for each product"
def getProductDetail(url):
    result = {}
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser') 
    result['title'] = soup.select('.h1')[0].text.strip()
    result['imgae'] = soup.select('#product-image img')[0]['src']
    result['description'] = soup.select('p')[0].text.strip()
    result['note'] = soup.select('p')[1].text.strip()
    return result

"A function getting product details for each page"
def parseListLinks(url):
    product_detail = []
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.select('.search-item-link'):
        product_detail.append(getProductDetail(link['href']))
    return product_detail
    
"Get all the product details"
url = 'https://www.luckyscent.com/category/17/womens?sort=new&sortdir=1&page={}'
product_total = []
for i in range(1, 53):
    producturl = url.format(i)
    productary = parseListLinks(producturl)
    product_total.extend(productary)
    print('page: ',i, ' done')

"Convert data to DataFrame"
df = pd.DataFrame(product_total)


import pickle
with open('perfume_data.pkl', 'wb') as f:
    pickle.dump(df,f)



