from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

websites = [
    {
        'name': 'Soompi',
        'url': 'https://www.soompi.com',
        'class': 'media-heading'
    },
]

search_query = 'BTS'
articles = []

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

for website in websites:
    print(f"Scraping {website['name']}...")
    url = f"{website['url']}/search?query={search_query}"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, website['class'])))

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    article_elements = soup.find_all('h4', website['class'])

    for article in article_elements:
        title = article.find('a').text.strip()
        link = article.find('a')['href']
        articles.append({'title': title, 'link': link})


for idx, article in enumerate(articles, 1):
    print(f"Article {idx}:")
    print("Title:", article['title'])
    print("Link:", article['link'])
    print("---")


driver.quit()