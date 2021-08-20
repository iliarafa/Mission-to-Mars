#!/usr/bin/env python
# coding: utf-8

# In[149]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import time 
import re


# In[150]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[151]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[152]:


html = browser.html
news_soup = bs(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[153]:


slide_elem.find('div', class_='content_title')


# In[154]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[155]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured images

# In[156]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[157]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[158]:


# Parse the resulting html with soup
html = browser.html
img_soup = bs(html, 'html.parser')


# In[159]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[160]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[161]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ['description','Mars','Earth']
df.set_index('description', inplace = True)
df


# In[162]:


df.to_html()


# In[163]:


#browser.quit()


# ## Visit the NASA Mars News Site

# In[164]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = bs(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## JPL Space Images Featured Image

# In[165]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# Parse the resulting html with soup
html = browser.html
img_soup = bs(html, 'html.parser')
img_soup
# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Mars Facts

# In[166]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df
df.to_html()


# ## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[167]:


### Hemispheres

# Visit URL
url = 'https://marshemispheres.com/'
browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# 3. Write code to retrieve the image urls and titles for each hemisphere.

html = browser.html
hsph_list = bs(html, 'html.parser')

items = hsph_list.find_all('div', class_='item')
items

for item in items:
    url_hr = item.find("a")['href']
    browser.visit(url+url_hr)
    
    hr_item_html = browser.html
    hr_soup = bs(hr_item_html, 'html.parser')
    
    title = hr_soup.find('h2', class_ = 'title').text

    downloads = hr_soup.find('div', class_ = 'downloads')
    image_url = downloads.find('a')['href']
    
    
    hemisphere_image_urls.append({"img url": url+image_url, "title": title, })


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()


# In[168]:


hemisphere_image_urls


# In[ ]:




