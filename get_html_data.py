#!/usr/local/bin/python3
import urllib.request
from bs4 import BeautifulSoup
from collections import namedtuple

Site = namedtuple("Site", ['url', 'image', 'title', 'publicat_de_pe', 'description', 'user', 'price', 'publicat_de'])

def get_user_input():
    """ Read user input from prompt
    e.g.:  add url:'https://www.olx.ro/oferta/duplex-de-vanzare-faget-cluj-ID91DKR.html#d31a30b111'
    """
    return input("add url:", )


def get_page_html(url):
    """

    :param url: get_user_input():
    :return:
    >>> get_page_html('https://www.olx.ro/oferta/duplex-de-vanzare-faget-cluj-ID91DKR.html#d31a30b111')
    soup
    """
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    soup.prettify()
    return soup


def get_page_by_identifier(soup, identifier):
    """
    :param soup: get_page_html(url) returns the page html
    :param identifier: id or css that will be searched
    >>> get_page_by_identifier(soup, 'photo-gallery-opener')
    soup.find(attrs='photo-gallery-opener').contents
    """
    return soup.find(attrs=identifier).contents


def get_page_attr_by_id(soup, html_id):
    return get_page_by_identifier(soup, {'id': [html_id]})


def get_page_attr_by_class(soup, html_class):
    return get_page_by_identifier(soup, {'class': [html_class]})


def olx_page(my_url):
    Site.url = my_url
    soup = get_page_html(Site.url)
    try:
        Site.title = get_page_attr_by_class(soup, 'offer-titlebox')[1].contents[0].strip()
    except IndexError:
        Site.title = "No Title"
    try:
        Site.image = get_page_attr_by_id(soup, 'photo-gallery-opener')[1].attrs['src']
    except IndexError:
        Site.image = "No Image"
    try:
        Site.publicat_de_pe = get_page_attr_by_class(soup, 'descriptioncontent')[8].text.strip()
    except IndexError:
        Site.publicat_de_pe = "No publish source"
    try:
        Site.description = get_page_attr_by_class(soup, 'descriptioncontent')[6].contents[1].contents[0].strip()
    except IndexError:
        Site.description = "No description"
    try:
        Site.user = get_page_attr_by_class(soup, 'offer-user__details')[1].text.strip()
    except IndexError:
        Site.user = "No User"
    try:
        Site.price = get_page_attr_by_class(soup, 'price-label')[1].contents[0]
    except IndexError:
        Site.price = "No Price"
    try:
        Site.publicat_de = get_page_attr_by_class(soup, 'descriptioncontent')[6].contents[1].contents[8].strip()
    except IndexError:
        Site.publicat_de = "Not Specified"
    return Site


def main_html():
    my_url = get_user_input()
    if 'olx' in my_url:
        return olx_page(my_url)




if __name__ == '__main__':
    main_html()
