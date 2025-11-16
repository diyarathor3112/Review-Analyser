import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

class EbayAdapter:
    def search_product(self, query):
        url = "https://ebay-data-scraper.p.rapidapi.com/products"
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "ebay-data-scraper.p.rapidapi.com"
        }
        params = {"query": query}

        try:
            response = requests.get(url, headers=headers, params=params)
            print("Ebay status:", response.status_code)
            if response.status_code != 200:
                print("Ebay response:", response.text)
                return []
            data = response.json()
            products = []
            for item in data.get("products", []):
                products.append({
                    "source": "eBay",
                    "title": item.get("title"),
                    "price": item.get("price"),
                    "rating": "N/A",
                    "reviews": "N/A",
                    "url": item.get("url"),
                    "image": item.get("image")
                })
            return products
        except Exception as e:
            print("Ebay error:", e)
            return []
