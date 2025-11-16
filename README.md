# 🛒 Review Analyzer

A Flask-based web application that aggregates product search results from multiple e-commerce platforms including Amazon, eBay, and Google. Get comprehensive product information, prices, ratings, and reviews all in one place.

## ✨ Features

- **Multi-Platform Search**: Search across Amazon, eBay, and Google simultaneously
- **Real-Time Results**: Fetch live product data from various sources
- **Responsive Web Interface**: Modern, mobile-friendly UI built with Bootstrap
- **Product Details**: View product titles, prices, ratings, and review counts
- **Direct Links**: Click through to view products on original platforms
- **Error Handling**: Graceful handling of API failures and network issues

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Chrome browser (for Selenium scraping)
- RapidAPI account with API keys for Amazon and eBay data

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd review-analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```
   RAPIDAPI_KEY=your_rapidapi_key_here
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open your browser:**
   Navigate to `http://localhost:5000`

## 📖 Usage

1. **Start the Application:**
   Run `python app.py` and visit `http://localhost:5000`

2. **Search for Products:**
   - Enter a product name in the search box (e.g., "iPhone 15", "Samsung TV")
   - Click the search button or press Enter

3. **View Results:**
   - Results are displayed in a table format
   - Each row shows source, product title, price, rating, and review count
   - Click "View Product" to visit the original listing

4. **API Endpoint:**
   You can also use the REST API directly:
   ```
   GET /search?query=your_product_name
   ```

## ⚙️ Configuration

### Environment Variables

- `RAPIDAPI_KEY`: Your RapidAPI key for accessing Amazon and eBay data APIs

### API Sources

- **Amazon**: Uses Real-Time Amazon Data API via RapidAPI
- **eBay**: Uses eBay Data Scraper API via RapidAPI
- **Google**: Uses Selenium for web scraping Google search results

## 📁 Project Structure

```
review-analyzer/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── utils.py                    # Utility functions
├── TODO.md                     # Development tasks
├── adapters/                   # Platform-specific adapters
│   ├── __init__.py
│   ├── amazon_adapter.py       # Amazon API integration
│   ├── ebay_adapter.py         # eBay API integration
│   └── generic_scrapper.py     # Google scraping with Selenium
└── templates/                  # HTML templates
    ├── index.html              # Main search interface
    └── results.html            # Results display (if used)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This application is for educational purposes only. Please respect the terms of service of the platforms being scraped and ensure compliance with API usage policies. Rate limiting and responsible scraping practices are implemented to minimize impact on source websites.

## 🐛 Troubleshooting

- **ChromeDriver Issues**: Selenium automatically manages ChromeDriver, but ensure Chrome browser is installed
- **API Key Errors**: Verify your RapidAPI key is correctly set in the `.env` file
- **Port Conflicts**: If port 5000 is busy, modify the port in `app.py`
- **Scraping Failures**: Google scraping may fail due to anti-bot measures; fallback dummy data is provided for testing

## 🔧 Development

To run in development mode with auto-reload:
```bash
export FLASK_ENV=development
python app.py
```

For debugging, check the console output for error messages from individual adapters.
