#!/user/bin/env/ python

import requests
from bs4 import BeautifulSoup
import pprint
import json 

url = 'https://www.humblebundle.com/books/programming-productivity-mercury-books'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# maybe better way of doing this is to try to get tada by the row

tiers = soup.select('.dd-game-row')
tier_dict ={}

for tier in tiers:
    #Only for section that have a headline
    if tier.select(".dd-header-headline"):
        #Grab tier name (and price)
        tiername = tier.select('.dd-header-headline')[0].text.strip()
        # Grab tier product names    
        product_name = tier.select(".dd-image-box-caption")
        product_name = [ prodname.text.strip().split("\n")[1] for prodname in product_name ]

        #Add one product row to ur dictionary
        tier_dict[tiername] ={"products" : product_name}


with open("file.json","w") as f:
    json.dump(tier_dict,f) 



# headers above each book colection

# this is one way to grab information but problem with this method is if in the future ownor deside to put another h2 tag into the current page,
# this culd break our code for this reasone we need to do this with the class selector.
# title_head = soup.find_all('h2')

#headline = soup.select('.dd-header-headline')
#dataHead = [line.text.strip() for line in headline]

# Get cost for each books

#Payment = [data.split(' ')[1] for data in dataHead if data.startswith('Pay')]

# Products name 
#product_name = soup.select('.dd-image-box-caption')
# stripped_product_name  = [name.text.strip().split('\n')[1] for name in product_name]





#for lineName, lineinfo in dataHead.items():
#    print(lineName)
#    print("priced at", ##########])
#    print("priduct name: ", lineinfo["priducts"])



 
# headline 1 name and price 
#  - product 1
#  - product 2
#  - product 4
#headline 2 name and price 
#  - product 1
#  - product 2
#  - product 4

# lins = {
#     "line1":{
#         "prince":200,
#         "products":[
#             "name1",
#             "name2"
#         ]
#         },
#         "line2":{
#         "prince":500,
#         "products":[
#             "name1",
#             "name2"
#         ]
#     }
# }
'







# as
# da
# sd
# a
# das
# d
# as
# das
# d
# as
# das
# d










