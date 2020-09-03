
import bs4
import requests
from urllib.error import HTTPError
from requests.exceptions import ConnectionError
from urllib.error import URLError


def urlopen(url):
    ''' 
    Chack if passed url has been correct. 

    Argument: 
        url - the web site address on which we want to sent request
    #Outpur:
        a text string that would give us information about correctness of URL        
    
    '''

    try:
        var ="no error"
        read = requests.get(url)
    except HTTPError as e:
        var = "error occured"
    except URLError as e:
        var = "error occured"
    except ConnectionError as e:
        var ="error occured"

    if (var =="no error"):
        return read
    else:
        return "error has occurred"




    