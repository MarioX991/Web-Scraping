import wsurlopen
from bs4 import BeautifulSoup
import lxml

var = wsurlopen.urlopen('https://www.aliexpress.com')
read = BeautifulSoup(var.text, "lxml")
print(read)