import urllib2
from bs4 import BeautifulSoup

def getListings(product):
	#takes in the product name, as a string, and outputs an array of tuples that is 200 items long or however many there are availible 
	#the tuples will be in the format {condition, price} 
	#the conditions will corrolate to numbers: New: 1, Refurbished: 2, Used: 3, For parts/Not working: 4
	data = []
	url = "https://www.ebay.com/sch/?_nkw=%22{}%22&LH_Sold=1&_ipg=200".format(product.replace(" ", "%20"))
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page,'html.parser')

	listings = soup.findAll("div", {"class": "s-item__info clearfix"})
	for listing in listings:
		price = filter(lambda x: x.isdigit() or x == ".", str(listing.find("span", {"class": "POSITIVE"})))
		condition = listing.find("span", {"class" : "SECONDARY_INFO"})
		if "Pre" in condition:
			condition = 3
		elif "New" in condition:
			condition = 1
		elif "Parts" in condition:
			condition = 4
		else:
			condition = 2
		data.append((condition, price))





	
