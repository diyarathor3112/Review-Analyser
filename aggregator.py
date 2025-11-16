import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# simple aggregator orchestration + ranking heuristic
class Aggregator:
    def __init__(self, adapters):
        """
        adapters: list of objects with .search(product_name) -> list of dict items
        each item: {source, title, price, currency, rating, review_count, url}
        """
        self.adapters = adapters

    def search(self, product):
        all_items = []
        # Use threadpool for parallel adapter calls (small number)
        with ThreadPoolExecutor(max_workers=len(self.adapters)) as ex:
            futures = {ex.submit(ad.search, product): ad for ad in self.adapters}
            for fut in as_completed(futures):
                ad = futures[fut]
                try:
                    items = fut.result(timeout=30)
                    if items:
                        all_items.extend(items)
                except Exception as e:
                    print(f"Adapter {ad} failed: {e}")

        # Normalize prices to a numeric value where possible (leave None if unknown)
        for it in all_items:
            it['price_value'] = self._to_float(it.get('price'))

        # Compute score for recommendation
        for it in all_items:
            it['score'] = self._score(it)

        best = None
        if all_items:
            # select best by highest score
            best = max(all_items, key=lambda x: x.get('score', 0))

        return {"items": all_items, "best": best}

    def _to_float(self, price):
        if price is None:
            return None
        try:
            # remove currency symbols, commas
            s = str(price)
            s = s.replace(",", "")
            # keep digits and dot, minus
            filtered = ''.join(ch for ch in s if (ch.isdigit() or ch in ".-"))
            return float(filtered)
        except:
            return None

    def _score(self, item):
        # Simple heuristic: lower price is better, higher rating + more reviews better.
        # Normalize components to combine. If price missing, penalize.
        pv = item.get('price_value')
        rating = item.get('rating') or 0
        reviews = item.get('review_count') or 0

        price_score = 0.0
        if pv is None:
            price_score = -1.0
        else:
            # inverse price: smaller price -> bigger score
            price_score = 1.0 / (1 + pv)

        rating_score = float(rating) / 5.0  # assume rating out of 5

        review_score = min(reviews / 500.0, 1.0)  # saturation after 500 reviews

        # weighted sum
        score = 0.6 * price_score + 0.3 * rating_score + 0.1 * review_score
        return score
