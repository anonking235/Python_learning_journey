from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from datetime import datetime
import time

driver = webdriver.Chrome()
articles_data = []
base_url = "https://news.ycombinator.com/"

for page in range(1, 4):
    print(f"\n--- Scraping Page {page} ---")
    if page == 1:
        url = base_url
    else:
        url = f"{base_url}?p={page}"

    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "titleline"))
        )
    except:
        print("Timeout")
        continue

    time.sleep(2)
    stories = driver.find_elements(By.CLASS_NAME, "titleline")
    print(f"Found {len(stories)} stories")

    for story in stories:
        try:
            link = story.find_element(By.TAG_NAME, "a")
            title = link.text
            url_href = link.get_attribute("href")
            if title and url_href:
                articles_data.append({
                    'title': title,
                    'url': url_href,
                    'page': page,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                print(f"✓ {title[:50]}...")
        except:
            continue

    time.sleep(2)

driver.quit()

with open('hn_multi_page.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'url', 'page', 'scraped_at'])
    writer.writeheader()
    writer.writerows(articles_data)

print(f"\nSaved {len(articles_data)} articles")
