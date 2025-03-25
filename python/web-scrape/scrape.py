import requests
from bs4 import BeautifulSoup

url = "https://example.com/"
response = requests.get(url)
response.raise_for_status()  
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

articles = soup.find_all('article')

article_data = [] 

for article in articles:
    
    title_element = article.find('h1')
    if title_element: 
        title = title_element.text.strip()
    else:
        title = "No title found"

    summary_element = article.find('p')
    if summary_element: 
        summary = summary_element.text.strip()
    else:
        summary = "No summary found"


    article_data.append({'title': title, 'summary': summary})

for item in article_data:
    print("Title:", item['title'])
    print("Summary:", item['summary'])
    print("-" * 20)  # Separator

# Optional:  Save to CSV or JSON

import csv
# CSV
csv_file = "output.csv"
csv_columns = ['title', 'summary']

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in article_data:
            writer.writerow(data)
    print(f"Data written to {csv_file}")

except IOError:
    print("I/O error")


