from flask import Flask, jsonify, request, render_template
from adapters.amazon_adapter import AmazonAdapter
from adapters.ebay_adapter import EbayAdapter
from adapters.generic_scrapper import GenericScraper
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# create class objects
amazon = AmazonAdapter()
ebay = EbayAdapter()
generic = GenericScraper()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Query parameter missing'}), 400

    results = []

    # Amazon
    try:
        amazon_results = amazon.search_product(query)
        results.extend(amazon_results)
    except Exception as e:
        print("Amazon Error:", e)

    # eBay
    try:
        ebay_results = ebay.search_product(query)
        results.extend(ebay_results)
    except Exception as e:
        print("eBay Error:", e)

    # Google / Generic
    try:
        generic_results = generic.search_product(query)
        results.extend(generic_results)
    except Exception as e:
        print("Generic Error:", e)

    if not results:
        return jsonify({'error': 'No results found'}), 404

    return jsonify(results)

if __name__ == '__main__':
    print("✅ Review Analyzer is Running! Use /search?query=iphone")
    app.run(debug=True)
