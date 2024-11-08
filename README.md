Zomato Restaurant Data Scraper
This script uses Selenium to scrape restaurant information from the Zomato NCR delivery page. It retrieves details such as restaurant name, rating, cuisine, cost for one, delivery time, available offers, and restaurant URL. The scraped data is saved to a CSV file for further analysis.

Requirements
Ensure that the following Python packages are installed:

selenium
webdriver_manager
pandas
You can install these packages using:

bash
Copy code
pip install selenium webdriver_manager pandas
Setup
Chrome Driver: This script uses Chrome as the browser for scraping. The webdriver_manager library is used to automatically manage the ChromeDriver, so make sure you have Chrome installed.

Page Scrolling: Zomato's site loads content dynamically. The scroll_page function scrolls down to load all restaurant listings before scraping.

Usage
Run the script. The script initializes a Chrome browser window and opens the Zomato NCR delivery page.

Scroll the Page: The scroll_page function scrolls through the Zomato page to ensure all data is loaded.

Scrape Data: The script extracts the following details from each restaurant container:

Restaurant Name
Rating
Cuisine
Cost for One
Delivery Time
Available Offers
URL link to the restaurant page
Save Data: Data is saved to zomato_restaurants.csv in the current directory.

Code Structure
scroll_page(driver): Scrolls down the Zomato page to load more restaurant data dynamically.
Data Extraction Loop: The loop iterates over each restaurant container, extracts the information, and appends it to lists.
Save to CSV: Data is saved to zomato_restaurants.csv using Pandas.
