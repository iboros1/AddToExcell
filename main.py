import urllib.request
from bs4 import BeautifulSoup
import openpyxl

# url1 = input("add url:", )
url = 'https://www.olx.ro/oferta/duplex-de-vanzare-faget-cluj-ID91DKR.html#d31a30b111'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

image_location = soup.find(attrs={'id': ['photo-gallery-opener']})
title_location = soup.find(attrs={'class':['offer-titlebox']})
content = soup.find(attrs={'class':['descriptioncontent']})
user_field = soup.find(attrs={'class':['offer-user__details']})

image = image_location.contents[1].attrs['src']
title = title_location.contents[1].contents[0].strip()
publicat_de_pe = content.contents[8].text.strip()
description = content.contents[6].contents[1].contents[0].strip()
user = user_field.contents[1].contents[1].contents[0].strip()

try:
    publicat_de = content.contents[6].contents[1].contents[8].strip()
except:
    publicat_de = "Not Specified"


wb = openpyxl.load_workbook("file.xlsx")
sheet = wb.get_sheet_by_name('Sheet1')

if sheet.cell(row = 1, column=7).value == None:
    print("Blank")
else:
    print("No blank")


print(image)
print(title)
print(publicat_de)
print(publicat_de_pe)
print(description)
print(user)


