import requests

def get_doi(author_name, paper_title):
    # Prepare the search query
    query = f"{paper_title} {author_name}"
    
    # Make the API request to CrossRef
    url = f"https://api.crossref.org/works"
    params = {
        "query.bibliographic": paper_title,
        "query.author": author_name,
        "rows": 1  # Limit results to 1 for efficiency
    }
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if any items were found
        if data["message"]["total-results"] > 0:
            # Extract DOI from the first result
            first_result = data["message"]["items"][0]
            title = first_result.get("title", ["N/A"])[0]
            doi = first_result.get("DOI", "N/A")
            
            # Print and return the DOI
            print(f"Title: {title}")
            print(f"DOI: {doi}")
            
            return doi
        else:
            print("No results found.")
    else:
        print(f"Error: {response.status_code}")
    
    return None

# Example usage
author_name = "Wenping Wang"
paper_title = "Advances in Artificial Intelligence and Machine Learning"
get_doi(author_name, paper_title)
