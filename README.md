# Headlines-Scraper-python-project-
This project is a simple web scraping script built using Python, Requests, and BeautifulSoup. It fetches the latest headlines from the Times of India homepage, extracts the text inside &lt;h2> tags, and saves them into a text file (headlines.txt).
The project demonstrates the ability to work with:

Web scraping using requests and BeautifulSoup

Parsing and extracting structured data from HTML

File handling in Python (writing data into .txt files)

⚙️ Features

✅ Fetches the homepage of Times of India

✅ Extracts headlines dynamically from <h2> tags

✅ Saves the headlines into a .txt file

✅ Displays the headlines in the terminal for quick viewing

🚀 Tech Stack

Python 3

Requests (for fetching web pages)

BeautifulSoup (bs4) (for parsing HTML)

📂 Output Example

headlines.txt will look like this:

Headline 1
Headline 2
Headline 3
...
And the terminal will display:

H2 tag Headline : Headline 1
H2 tag Headline : Headline 2
...

🔧 How to Run
Clone the repository

git clone https://github.com/your-username/times-of-india-scraper.git
cd times-of-india-scraper

Install dependencies
pip install requests beautifulsoup4


Run the script
python scraper.py

📌 Use Cases
Collecting news headlines for quick reading

Practicing web scraping and text extraction

A base project for advanced scraping (news summaries, sentiment analysis, etc.)
