#!/usr/bin/env python
# coding: utf-8

# In[161]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install webdriver_manager')


# In[162]:


#importing libraries 

from selenium import webdriver
import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver # used to control web browsers programmatically
from selenium.webdriver.chrome.service import Service #used to manage the lifecycle of the ChromeDriver service.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
import pandas as pd 
import time 
import csv


# In[163]:


#initialize the chrome Driver 
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))


# In[164]:


driver.get("https://www.zomato.com/ncr/delivery")


# In[165]:


def scroll_page(driver):
    # Scroll down the page to load all elements dynamically
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)  # Allow time for the page to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        
# Use this function before finding elements
#scroll_page(driver)


# In[166]:


# Number of rows we want to scrap - 
target_rows = 300


# In[167]:


wait = WebDriverWait(driver, 10)


# In[168]:


print("Scrolling page...")
scroll_page(driver)
print("Scrolling complete, looking for containers...")


# In[72]:





# In[169]:


# Initialize lists to store the extracted data
restaurant_name = []
ratings = []
cuisine_type = []
cost_for_one = []
delivery_time = []
offers = []
urls = []


try:
    containers = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//div[contains(@class, "sc-cLxPOX") and contains(@class, "fhurJM")]')))
    print(f"Found {len(containers)} containers")
except TimeoutException:
    print("Containers not found")
    containers = []


# Extract data from each element
for box in containers:
    try:
        name = box.find_element(By.TAG_NAME, "h4").text
    except:
        name = 'N/A'
    
    try:
        rating = box.find_element(By.XPATH, ".//div[@class='sc-1q7bklc-1 cILgox']").text
    except:
        rating = 'N/A'
    
    try:
        cuisine = box.find_element(By.XPATH, ".//p[@class='sc-1hez2tp-0 sc-ibnDSj hLKVRh']").text
    except:
        cuisine = 'N/A'
    
    try:
        cost = box.find_element(By.CSS_SELECTOR, "p.sc-1hez2tp-0.sc-ibnDSj.ghswyr").text
    except:
        cost = 'N/A'
    
    try:
        time = box.find_element(By.XPATH, ".//div[@class='min-basic-info-right']").text
    except:
        time = 'N/A'
    
    try:
        offer = box.find_element(By.XPATH, ".//p[@class='sc-1hez2tp-0 sc-esoVGF dPOEfH']").text
    except:
        offer = 'No Offers'
    
    try:
        link = box.find_element(By.TAG_NAME, 'a').get_attribute('href')
    except:
        link = "N/A"
    
    # Append data to the corresponding lists
    restaurant_name.append(name)
    ratings.append(rating)
    cuisine_type.append(cuisine)
    cost_for_one.append(cost)
    delivery_time.append(time)
    offers.append(offer)
    urls.append(link)
 
    # Check if we have reached the target number of rows
    if len(restaurant_name) >= target_rows:
        break
        
#Close the driver 
#driver.quit()


# In[ ]:





# In[170]:


print(restaurant_name)


# In[171]:


print(ratings)


# In[172]:


print(cuisine_type)


# In[173]:


print(cost_for_one)


# In[174]:


print(delivery_time)


# In[175]:


print(offers)


# In[176]:


print(urls)


# In[178]:


data = {
    'Restaurant Name': restaurant_name,
    'Rating': ratings,
    'Cuisine': cuisine_type,
    'Cost for One': cost_for_one,
    'Delivery Time': delivery_time,
    'Offers': offers,
    'Link': urls
}


# In[179]:


df = pd.DataFrame(data)


# In[182]:


df.to_csv('zomato_restaurants.csv', index=False, encoding='utf-8')
df


# In[181]:


print("Data saved to zomato_restaurants.csv")


# In[ ]:




