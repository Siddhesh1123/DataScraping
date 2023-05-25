import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

if __name__ == '__main__':
 Header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
           'Accept-Language': 'en-US, eb; \q=0.5'})
 
 req = requests.get("https://www.amazon.in/s?k=bags&ref=sr_pg_1",headers=Header)
 
 soup = BeautifulSoup(req.content, "html.parser")
 
 links = soup.findAll('a', attrs={
                      'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
# Store the links
 links_list = []
 # Loop for extracting links from Tag Objects
 for link in links:
     links_list.append(link.get('href'))

 d = {"title": [], "price": [], "rating": [], "reviews": [], "availability": []}
 # Products URL
 links = soup.find_all('a', attrs={
                       'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
 # print(links) of 20 product first
 for i in links_list:
   new_webpage = requests.get("https://www.amazon.com" + link, headers=Header)
   new_soup = BeautifulSoup(new_webpage.content, "html.parser")
 

 # print(new_soup)
 
 # Product Name
 def get_title(soup):
  title = new_soup.find("span", attrs={'id': 'productTitle'})
  print(title)
 
 # Product Price
 
 
 def get_price(soup):
  Prize = new_soup.find("span", attrs={
                       'class': 'a-price-whole'}).find("span", attrs={'class': 'a-price-whole'})
  print(Prize)
 
 #Ratings
 
 
 def get_rating(soup):
  Rating = new_soup.find("span", attrs={
     'class': 'a-popover-trigger a-declarative'})
  print(Rating)
 
 #Number of reviews
 def get_review_count(soup):
  reviews = new_soup.find("span", attrs={
     'id': 'acrCustomerReviewText'})
  print(reviews)
 
 d['title'].append(get_title(new_soup))
 d['price'].append(get_price(new_soup))
 d['rating'].append(get_rating(new_soup))
 d['reviews'].append(get_review_count(new_soup))

 amazon_df = pd.DataFrame.from_dict(d)
 amazon_df['title'].replace('', np.nan, inplace=True)
 amazon_df = amazon_df.dropna(subset=['title'])
 amazon_df.to_csv("amazon_data.csv", header=True, index=False)

 print(amazon_df)
