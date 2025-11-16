import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

class AmazonAdapter:
    def search_product(self, query):
        url = "https://real-time-amazon-data.p.rapidapi.com/search"
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
        }
        params = {
            "query": query,
            "country": "IN"
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            print("Amazon status:", response.status_code)
            if response.status_code != 200:
                print("Amazon response:", response.text)
                return []
            data = response.json()
            products = []
            for item in data.get("data", {}).get("products", []):
                products.append({
                    "source": "Amazon",
                    "title": item.get("product_title"),
                    "price": item.get("product_price"),
                    "rating": "N/A",
                    "reviews": "N/A",
                    "url": item.get("product_url"),
                    "image": item.get("product_photo")
                })
            return products
        except Exception as e:
            print("Amazon error:", e)
            return []
