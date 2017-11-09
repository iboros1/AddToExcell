import urllib.request
from bs4 import BeautifulSoup


url = input("add url:", )
#url = 'https://www.olx.ro/oferta/duplex-de-vanzare-faget-cluj-ID91DKR.html#d31a30b111'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

image_location = soup.find(attrs={'id': ['photo-gallery-opener']})
title_location = soup.find(attrs={'class':['offer-titlebox']})
content = soup.find(attrs={'class':['descriptioncontent']})
user_field = soup.find(attrs={'class':['offer-user__details']})
price_label = soup.find(attrs={'class':['price-label']})

image = image_location.contents[1].attrs['src']
title = title_location.contents[1].contents[0].strip()
publicat_de_pe = content.contents[8].text.strip()
description = content.contents[6].contents[1].contents[0].strip()
user = user_field.contents[1].contents[1].contents[0].strip()
price = price_label.contents[1].contents[0]

try:
    publicat_de = content.contents[6].contents[1].contents[8].strip()
except:
    publicat_de = "Not Specified"




print(image)
print(title)
print(publicat_de)
print(publicat_de_pe)
print(description)
print(user)


