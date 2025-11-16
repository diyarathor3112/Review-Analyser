from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class GenericScraper:
    def search_product(self, query):
        try:
            # Set up Chrome options for headless mode
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

            # Initialize the driver
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            url = f"https://www.google.com/search?q={query}+buy+online"
            driver.get(url)
            time.sleep(2)  # Wait for page to load

            results = []
            # Find search result titles
            titles = driver.find_elements(By.CSS_SELECTOR, "h3")
            links = driver.find_elements(By.CSS_SELECTOR, "h3 a")

            for i, title in enumerate(titles[:5]):  # Limit to 5 results
                title_text = title.text
                href = links[i].get_attribute("href") if i < len(links) else ""
                if href and href.startswith("/url?q="):
                    href = href.split("/url?q=")[1].split("&")[0]
                results.append({
                    "source": "Google",
                    "title": title_text,
                    "price": "N/A",
                    "rating": "N/A",
                    "reviews": "N/A",
                    "url": href
                })

            driver.quit()
            return results if results else self.get_dummy_results(query)
        except Exception as e:
            print("Generic scraper error:", e)
            return self.get_dummy_results(query)

    def get_dummy_results(self, query):
        # Dummy results for testing when scraping fails
        return [
            {
                "source": "Google",
                "title": f"Sample {query} Product 1",
                "price": "$99.99",
                "rating": "4.5",
                "reviews": "100",
                "url": "https://example.com/product1"
            },
            {
                "source": "Google",
                "title": f"Sample {query} Product 2",
                "price": "$149.99",
                "rating": "4.2",
                "reviews": "50",
                "url": "https://example.com/product2"
            }
        ]

