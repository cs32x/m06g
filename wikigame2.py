### m06/wikigame2.py
import requests
import json

def grab_links(title):
    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'https'
    hostname = 'en.wikipedia.org'
    path = '/w/api.php'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'action': 'parse',
             'page': title,
             'prop': 'links',
             'section': 0,
             'format': 'json'
    }

    response = requests.get(url, params=query, headers={'user-agent':'cs32x educational demo'})

    # Read the response body in JSON format
    j = response.json()

    print()

    # Print titles of links from response body
    links_data = j["parse"]["links"]
    links = [l["*"] for l in links_data if l["ns"] == 0]
    for i, link in enumerate(links):
        print(i, link)
    
    print()

    return links

def main():
    links = grab_links('The Cat in the Hat')

if __name__ == '__main__':
    main()