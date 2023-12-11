import requests
from bs4 import BeautifulSoup
import csv

# Base URL of the website with pagination parameter
base_url = 'https://www.darimooch.com/collections/all-products?page={}'

# Number of pages you want to scrape
num_pages = 5

# Write data to CSV file
with open('product_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product Name', 'Price', 'Rating'])

    for page_num in range(1, num_pages + 1):
        # Form the URL with the current page number
        url = base_url.format(page_num)

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract information (modify this part based on the structure of the website)
            names = soup.find_all('h3', class_='product-card__title f-family--heading f-caps--false f-space--0')
            prices = soup.find_all('p', class_='price')
            ratings = soup.find_all('div', class_='review-wrapper')

            # Write data to CSV file
            for name, price, rating in zip(names, prices, ratings):
                csv_writer.writerow([name.text.strip(), price.text.strip(), rating.text.strip()])

            print(f'Data from page {page_num} has been successfully saved.')
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
