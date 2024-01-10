# multiple-page-webscraper
1. Import the necessary libraries: requests for making HTTP requests and BeautifulSoup for parsing HTML content.

1. Specify the root URL of the website and the initial URL to scrape.

1. Send an HTTP GET request to the specified URL (website) and store the HTML response.

1. Parse the HTML content of the page using BeautifulSoup with the 'lxml' parser.

1. Print the prettified HTML content (for debugging purposes).

1. Find the main article element on the page with the class 'main-article'.

1. Extract all movie links from the main article using anchor tags.

1. Print the list of movie links (for debugging purposes).
   
1. Iterate over each movie link and perform the following steps for each movie:
   * Send an HTTP GET request to the movie page.
   * Parse the HTML content of the movie page using BeautifulSoup.
   * Find the main article element on the movie page.
   * Extract the movie title from the H1 heading.
   * Extract the transcript from the div with class 'full-script'.
   * Write the transcript to a text file with the movie title as the filename.

* Note: This script assumes a specific HTML structure on the website, and any changes to the website's structure may require adjustments to the script. Additionally, web scraping should be done responsibly, respecting the website's terms of service and legal considerations.
