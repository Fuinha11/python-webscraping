from urllib.request import urlopen
from bs4 import BeautifulSoup

def do_thing():
    url = "https://alura-site-scraping.herokuapp.com/hello-world.php"
    response = urlopen(url) # Get on url
    html = response.read() # Read the html data from response
    soup = BeautifulSoup(html, 'html.parser') # Parse HTML to a Beautiful Soup OBJ
    print(soup.find('h1', id='hello-world').get_text()) # Find the desired tag
    print(soup.find('p').get_text())
    

if __name__ == "__main__":
    do_thing()


