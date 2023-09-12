# Google-Allintitle-Search-Scraper
This Python script allows you to scrape Google search results using the "allintitle:" operator. It retrieves the total number of search results for a list of keywords and saves the results to an Excel file for further analysis. This can be especially useful for SEO professionals, marketers, or anyone interested in monitoring keyword competition.

**Features**
Scrapes Google search results for multiple keywords using "allintitle:"
Handles rate limiting by waiting between requests
Retry mechanism for failed requests
Saves results to an Excel file for easy analysis
Getting Started
Follow these steps to set up and use the Google Allintitle Search Scraper:

**Step 1:** Clone the Repository
Clone this repository to your local machine using the following command:

_**git clone https://github.com/your-username/your-repository.git**_

**Step 2:** Install Dependencies
Make sure you have Python 3.x installed on your system. Install the required libraries using pip:

_**pip install requests pandas**_

**Step 3:** Configure Google API Key and Custom Search Engine ID
Open the script in a text editor and replace the placeholders with your Google API Key and Custom Search Engine ID.

# Define your Google API key and Custom Search Engine ID here
_**GOOGLE_API_KEY = "YOUR_API_KEY"**_
_**CSE_ID = "YOUR_CSE_ID"**_

**Step 4:** Prepare Your Input File
Create a text file (e.g., keywords.txt) containing the list of keywords you want to search for, with each keyword on a separate line.

**Step 5:** Run the Script
Execute the script by running the following command in your terminal:

_**python google_allintitle_scraper.py**_

The script will prompt you to enter the path to the input file (e.g., keywords.txt). After entering the path, it will start scraping Google search results for each keyword.

Step 6: View the Results
Once the script completes all queries, it will save the results to an Excel file named allintitle_results.xlsx in the same directory as the script. You can open this file to analyze the data.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This script uses the Google Custom Search JSON API to retrieve search results.
Thank you for using the Google Allintitle Search Scraper! If you find it helpful, please consider giving it a star on GitHub and sharing it with others.














