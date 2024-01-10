import requests  # Import the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing

# Specify the root URL of the website and the initial URL to scrape
root = 'https://subslikescript.com'
website = f'{root}/movies'

# Send an HTTP GET request to the specified URL and store the response
result = requests.get(website)
content = result.text

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Print the prettified HTML content (for debugging purposes)
print(soup.prettify())

# Find the main article element on the page
box = soup.find('article', class_='main-article')

# Extract all movie links from the main article
links = [link['href'] for link in box.find_all('a', href=True)]

# Print the list of movie links (for debugging purposes)
print(links)

# Iterate over each movie link and extract the transcript
for link in links:
    # Send an HTTP GET request to the movie page
    result = requests.get(f'{root}/{link}')
    content = result.text

    # Parse the HTML content of the movie page using BeautifulSoup
    soup = BeautifulSoup(content, 'lxml')

    # Find the main article element on the movie page
    box = soup.find('article', class_='main-article')

    # Extract the movie title from the H1 heading
    title = box.find('h1').get_text()

    # Extract the transcript from the div with class 'full-script'
    transcript = box.find('div', class_='full-script')
    transcript = transcript.get_text(strip=True, separator=' ')

    # Write the transcript to a text file with the movie title as the filename
    with open(f'{title}.txt', 'w', encoding="utf-8") as f:
        f.write(transcript)
