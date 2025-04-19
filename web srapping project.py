import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

URL= 'https://www.jiomart.com/c/groceries/2'

page = requests.get(URL)
page.status_code

htmlCode = page.text
soup = BeautifulSoup(htmlCode)
htmlCode

name = soup.find('div', attrs={'class' : 'plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80'})
print(name.text)
name = name.text
x = name.strip()
print(x)

price = soup.find('span', attrs={'class' : 'jm-heading-xxs jm-mb-xxs'})
print(price.text)
price = price.text
x = price.strip()
print(x)


res_names = []
names = soup.find_all('div', attrs={'class' : 'plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80'})


for i in names:
    x = i.text
    x = x.strip()
    res_names.append(x)
print(res_names)
print(len(res_names))


res_prices = []
prices = soup.find_all('span', attrs={'class' : 'jm-heading-xxs jm-mb-xxs'})
for i in prices:
    x = i.text
    x = x.strip()
    res_prices.append(x)
print(res_prices)
print(len(res_prices))

details = soup.find('div', attrs={'class' : 'plp-card-details-container'})
print(details.text)
name = details.text
x = name.strip()
print(x)

res_details = []
details = soup.find_all('div', attrs={'class': 'plp-card-details-container'})
# Extract and clean the text content
for item in details:
    res_details.append(item.text.strip())

main = []
for detail in res_details:
    parts = detail.split("    ")
    if len(parts) == 3:
        name = parts[0].strip()
        prices = parts[1].split("  ")
        discount = parts[2].strip()
        if len(prices) == 2:
            main.append([name, prices[0], prices[1], discount])
names = [item[0] for item in main]
discounted_prices = [item[1] for item in main]
actual_prices = [item[2] for item in main]
discount_percents = [item[3] for item in main]
final_discounted_prices = [price.replace("₹", "").replace(",", "") for price in discounted_prices]
final_actual_prices = [price.replace("₹", "").replace(",", "") for price in actual_prices]
# Print results for verification
print(names)
print(len(names))
print(final_discounted_prices)
print(len(final_discounted_prices))
print(final_actual_prices)
print(len(final_actual_prices))
print(discount_percents)
print(len(discount_percents))
# create a dataframe[applying pandas]
df = pd.DataFrame({'Product' : names , 'Discounted Price': final_discounted_prices , 'Actual Price' : final_actual_prices , 'Discount Percent' : discount_percents})
df['Discounted Price'] = df['Discounted Price'].astype(float)
df['Actual Price'] = df['Actual Price'].astype(float)
print(df)
# applying matplotlib
plt.hist(df['Discounted Price'], bins = 2, color='green', alpha=0.4)
plt.title('Price Variation')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()
# applying matplotlib
plt.pie(df['Discounted Price'], labels=df['Product'], autopct = '%1.2f%%', startangle = 180)
plt.axis('equal')
plt.show()
# saving the dataframe
df.to_excel('project.xlsx', header=True, index=True)
import os
os.startfile("project.xlsx")

