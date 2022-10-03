import requests

URL = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"

response = requests.get(URL)
with open('steeleye.xml', 'wb') as file:
    file.write(response.content)

