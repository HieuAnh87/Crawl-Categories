from bs4 import BeautifulSoup
from urllib import request
import urllib.request
import config
from distlib.compat import raw_input

# site = input("Type the name of the website")
site = raw_input("Type the name of the website")
# Takes the website you typed and stores it in > site < variable
make_request_to_site = request.urlopen(site).read()
# Makes a request to the site that we stored in a var
soup = BeautifulSoup(make_request_to_site, "html.parser")
# We pass it through BeautifulSoup parser in this case html.parser
# We will take config òf the site
tag = config.domain[site][0]
class1 = config.domain[site][1]
# Next we make a loop to find all links in the site that we stored
for link in soup.find(tag, class_=class1).findAll('a'):
    print(link['href'])



