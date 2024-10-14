import requests
from bs4 import BeautifulSoup
import re

def scrape_publication_details(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator=' ')  # Extract all text from the page
    
    # Regex pattern to find the abstract
    abstract_pattern = re.compile(r'(abstract|summary|overview)\s*[:\-–]*\s*(.*)', re.IGNORECASE)
    abstract_match = re.search(abstract_pattern, text)
    abstract = abstract_match.group(2).strip() if abstract_match else "Abstract not found"
    
    # Regex pattern to find the citation count
    citation_pattern = re.compile(r'(cited by|citations|cites)\s*[:\-–]*\s*(\d+)', re.IGNORECASE)
    citation_match = re.search(citation_pattern, text)
    citation_count = citation_match.group(2).strip() if citation_match else "Citations not found"
    
    return {
        "abstract": abstract,
        "citation_count": citation_count
    }

# Example usage
link = input("Enter the publication link: ")
details = scrape_publication_details(link)

print(f"Abstract: {details['abstract']}")
print(f"Citations: {details['citation_count']}")
