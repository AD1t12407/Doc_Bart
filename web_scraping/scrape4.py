import requests

def get_doi(author_name, paper_title):
    # Format the query parameters for author and title
    query = f"author:{author_name}: title:{paper_title}:"
    
    # Make the API request to DBLP
    url = f"https://dblp.org/search/publ/api?q={query}&format=json"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if there are any hits
        if data["result"]["hits"]["@total"] != "0":
            # Loop through the hits to find the DOI
            for hit in data["result"]["hits"]["hit"]:
                info = hit["info"]
                title = info.get("title", "N/A")
                doi = info.get("doi", "N/A")
                
                # Print the title and DOI
                print(f"Title: {title}")
                print(f"DOI: {doi}")
                
                return doi
        else:
            print("No results found.")
    else:
        print(f"Error: {response.status_code}")
    
    return None

get_doi("Getinet Yilma","Advances in Artificial Intelligence and Machine Learning (AAIML)")