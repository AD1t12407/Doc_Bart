import requests
from bs4 import BeautifulSoup

def scrape_google_scholar(faculty_name, year=None, domain=None, title=None):
    # Construct the search query
    query = faculty_name
    if year:
        query += f" {year}"
    if domain:
        query += f" {domain}"
    if title:
        query += f" {title}"
    
    # Replace spaces with "+" for the URL
    search_url = f"https://scholar.google.com/scholar?q={query.replace(' ', '+')}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract publication details
    publications = []
    for result in soup.select('.gs_ri'):
        pub_title = result.select_one('.gs_rt').text
        link = result.select_one('.gs_rt a')['href']
        snippet = result.select_one('.gs_rs').text
        publication_info = result.select_one('.gs_a').text
        
        # Filter by year if provided
        if year and str(year) not in publication_info:
            continue
        
        # Filter by domain if provided
        if domain and domain.lower() not in snippet.lower():
            continue
        
        # Filter by title if provided
        if title and title.lower() not in pub_title.lower():
            continue

        # Scrape additional information from the link
        additional_info = scrape_publication_details(link)
        
        publication = {
            "title": pub_title,
            "link": link,
            "snippet": snippet,
            "additional_info": additional_info
        }
        
        publications.append(publication)
    
    return publications

def scrape_publication_details(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract abstract (This will vary based on the website)
    abstract = soup.find('div', class_='abstract').text if soup.find('div', class_='abstract') else "Abstract not found"
    
    # Extract citation count (Example: "Cited by 500")
    citation_count = soup.find('a', text=lambda x: x and 'Cited by' in x)
    citation_count = citation_count.text if citation_count else "Citations not found"
    
    # Extract any other details you might need
    # Example:
    # published_date = soup.find('span', class_='published-date').text if soup.find('span', class_='published-date') else "Date not found"

    return {
        "abstract": abstract,
        "citation_count": citation_count,
        # Add more fields if necessary
    }

# Get user input
faculty_name = input("Enter the faculty name: ")
year = input("Enter the publication year (leave blank if not applicable): ")
domain = input("Enter the domain (leave blank if not applicable): ")
title = input("Enter the title (leave blank if not applicable): ")

# Convert year to integer if provided
year = int(year) if year else None

# Scrape Google Scholar
results = scrape_google_scholar(faculty_name, year=year, domain=domain, title=title)

# Display results
for pub in results:
    print(f"Title: {pub['title']}\nLink: {pub['link']}\nSnippet: {pub['snippet']}\n")
    print(f"Abstract: {pub['additional_info']['abstract']}\nCitations: {pub['additional_info']['citation_count']}\n")
