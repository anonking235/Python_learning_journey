import requests
from bs4 import BeautifulSoup

#In the first step, we will fetch the url
url = "http://quotes.toscrape.com"
response = requests.get(url)

# In the second step we would parse the Html
soup = BeautifulSoup(response.content, "html.parser")

#In step 3, we find all the quotes

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

#In step 4 we print first 5 quotes.

print("quotes and Authors:")
for i, (quote, author) in enumerate(zip(quotes[:5], authors[:5])):
    print(f"{i+1}. {quote.text} - {author.text}")

#And we are done.
#did the challenge part too

import csv

#open a file to write
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    #write header
    writer.writerow(['Quote', 'Author'])

    #Write data
    for quote, author in zip(quotes[:5], authors[:5]):
        writer.writerow([quote.text, author.text])

print("Data saved in quotes.csv")

