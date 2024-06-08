from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Create a Service object using ChromeDriverManager
service = Service(ChromeDriverManager().install())


# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)
driver.get("https://www.freshmenu.com/")
driver.implicitly_wait(10)
dish_name = driver.find_elements(By.CSS_SELECTOR,'h3.fm-product-new--body--title.ng-binding.ng-scope')

name_of_the_item = []
for ele in dish_name:
  name_of_the_item.append(ele.text)
print(name_of_the_item)
print(len(name_of_the_item))

price_of_the_item = []
price = driver.find_elements(By.CSS_SELECTOR,"span.new.ng-binding")
for p in price:
    price_of_the_item.append(p.text)
print(price_of_the_item)
elements = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/product/"]')
urls =[]
for ele in elements:
    url = ele.get_attribute('href')
    urls.append(url)
print(urls)
    
driver.quit()
data = {
    'Dish Name': name_of_the_item,
    'Price': price_of_the_item,
    'url_of_food_the_Item':urls
    
}
for key, value in data.items():
    print(f"Length of {key}: {len(value)}")

# Ensure all lists/arrays are the same length
min_length = min(len(value) for value in data.values())
for key in data.keys():
    if len(data[key]) != min_length:
        print(f"Adjusting length of {key} from {len(data[key])} to {min_length}")
        data[key] = data[key][:min_length]

# Create the DataFrame
df = pd.DataFrame(data)
print(df)


# Save the DataFrame to a CSV file
df.to_csv('freshmenu_items.csv', index=False)
