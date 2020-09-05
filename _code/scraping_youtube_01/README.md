# Readme for code1.

For this task, we scraped the website https://www.humblebundle.com/, but not the whole site just the book section. From which we gabbed information about book name, price of the book, and headers.


The Scraped data has stored as a JSON file with the structure presented below:

# data = {
#     "header1":{
#         "prince":200,
#         "products":[
#             "name1",
#             "name2"
#         ]
#         },
#         "headerw":{
#         "prince":500,
#         "products":[
#             "name1",
#             "name2"
#         ]
#     }
#    .......

# }


#TODO
1. we are capturing "SUPPORT CHARITY" by headline
2. product name contain one additional element that we need to rid of named as "Locked content"


## Set up dev enviroment
    virtualenv -p pytho3 venv

## Activate it
    source venv/bin/activate
