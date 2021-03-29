from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

def clean_input(input):
    return " ".join(input.split()).replace('> <', '><')

url = 'https://alura-site-scraping.herokuapp.com/index.php'
headers = {'User-Agent': 'Chrome/76.0.3809.100'} # Creating a headers dictionary.

req = Request(url, headers = headers) # Creating the request using the headers dictionary.
response = urlopen(req)
b = response.read()

html = clean_input(b.decode('utf-8')) # Decoding and cleaning.

soup = BeautifulSoup(html, 'html.parser') # Parsing.

cards = [] # Array to hold all cards.
card = {} # Dictionary to store the information.

anuncio = soup.find('div', {'class': 'well card'}) # Find one add in the page.

infos = anuncio.find('div', {'class':'body-card'}).find_all('p') # Find the infos inside a body of card.

for info in infos:
    card[info.get('class')[0].split('-')[-1]] = info.get_text() # Storing infos to dict dynamicaly.

card['valor'] = anuncio.find('p',{'class':'txt-value'}).get_text() # Storing more info from other divs

items = anuncio.find('div', {'class':'body-card'}).ul.find_all('li') # Find the accessories inside a body of card.

items.pop() # Removing last item '...'

accessories = [] # Create array for accessories

for a in items :
        accessories.append(a.get_text().replace('► ', '')) # Adding acessories in array

card['accessories'] = accessories # Adding to dict

dataset = pd.DataFrame.from_dict(card, orient = 'index').T # Creating a data Frame from our card data.
dataset.to_csv('./output/data/dataset.csv', sep=';', index = False, encoding = 'utf-8-sig') # exporting the info.

image = anuncio.find('div', {'class':'image-card'}).find('img') # Find the image inside the card.
urlretrieve(image.get('src'), './output/img/' + image.get('src').split('/')[-1]) # Downloading the image to a data folder