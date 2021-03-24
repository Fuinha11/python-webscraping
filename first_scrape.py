from urllib.request import urlopen
from bs4 import BeautifulSoup

def do_thing():
    url = "https://alura-site-scraping.herokuapp.com/hello-world.php"
    response = urlopen(url).read()
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.find('h1', id='hello-world').get_text())
    print(soup.find('p').get_text())
    

if __name__ == "__main__":
    do_thing()


