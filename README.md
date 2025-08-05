Web Scraper for News Headlines

This is a simple Python project created for the **Python Developer Internship** program under the Ministry of MSME, Govt. of India.

Task Objective

To **scrape top news headlines** from a news website and save them into a `.txt` file using Python.

Tools & Libraries Used
- Python
- `requests` (for fetching the webpage)
- `BeautifulSoup` (for parsing HTML)

How It Works
The script:
1. Fetches the HTML content of a news website (e.g., BBC News).
2. Parses the page to extract news headlines (`<h2>` or `<h3>` tags).
3. Filters, cleans, and saves the headlines into a `headlines.txt` file.

Project Structure
├── news_scraper.py # Main Python script
├── headlines.txt # Output file containing scraped headlines
└── README.md # This file


Setup Instructions
1. Clone the repository or download the files.
2. Install the required Python libraries:


pip install requests beautifulsoup4

Run the script:
python news_scraper.py

Check the headlines.txt file for the scraped headlines.

Sample Output
python-repl
Copy code
Breaking: Major earthquake hits Japan
India wins gold at the Asian Games
Tech giants announce AI alliance

Notes
The current script scrapes headlines from BBC News. You can change the URL in the script to target a different website.

Ensure the website you're scraping allows it by checking their robots.txt file or terms of use.

Outcome
Automated data collection of live news headlines from a public news website — helpful for beginners in web scraping, data collection, and automation tasks using Python.

