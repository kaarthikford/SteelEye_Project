from bs4 import BeautifulSoup

# Reading the data inside the xml
# file to a variable under the name
# data
with open('steeleye.xml', 'r') as f:
	data = f.read()

# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")

# Finding all instances of tag
# `result`
result = Bs_data.find_all('result')

print(result)

# Using find() to extract attributes
# of the first instance of the tag
link = Bs_data.find('str', {'name':'download_link'}).text

print(link)

import wget
url=link
wget.download(url)
