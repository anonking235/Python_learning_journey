
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from datetime import datetime
import time

driver = webdriver.Chrome()
driver.get("https://www.bbc.com/news")

# Wait for the main content to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class, 'sc-')]"))
    )
except:
    print("Timeout")

time.sleep(2)

# Use XPath to find all h2 headlines (more reliable)
headlines = driver.find_elements(By.XPATH, "//h2")

print(f"Found {len(headlines)} headlines\n")

articles_data = []
for headline in headlines[:10]:
    try:
        title = headline.text.strip()

        # Find the closest link ancestor
        link = headline.find_element(By.XPATH, ".//ancestor::a | ./ancestor::a")
        url = link.get_attribute("href")

        if title and url and len(title) > 5:  # Filter out empty/short titles
            articles_data.append({
                'title': title,
                'url': url,
                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            print(f"✓ {title[:60]}...")
    except:
        continue

driver.quit()

with open('news_articles.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'url', 'scraped_at'])
    writer.writeheader()
    writer.writerows(articles_data)

print(f"\nSaved {len(articles_data)} articles to news_articles.csv")
