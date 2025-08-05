import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

response = requests.get(URL)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

headlines = soup.find_all(['h3', 'h2'])  

headline_list = []
for headline in headlines:
    text = headline.get_text(strip=True)
    if text and len(text) > 10:  
        headline_list.append(text)

unique_headlines = list(dict.fromkeys(headline_list))[:10]

with open("headlines.txt", "w", encoding='utf-8') as file:
    for headline in unique_headlines:
        file.write(headline + "\n")

print("Top headlines saved to 'headlines.txt'")
