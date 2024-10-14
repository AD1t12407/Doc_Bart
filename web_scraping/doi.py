import requests

def get_abstract_from_doi(doi):
    # CrossRef API endpoint for DOI lookup
    url = f"https://api.crossref.org/works/{doi}"
    
    # Make the request to CrossRef API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Try to get the abstract from the metadata
        abstract = data['message'].get('abstract', 'No abstract found.')
        
        return abstract
    else:
        return f"Error: {response.status_code}"

# Example usage
doi = " 10.31483/r-98432"  # Replace with your DOI
abstract = get_abstract_from_doi(doi)

print(f"Abstract: {abstract}")
