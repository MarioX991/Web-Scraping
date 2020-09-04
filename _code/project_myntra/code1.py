import wsurlopen
from bs4 import BeautifulSoup
import lxml

var = wsurlopen.urlopen('https://www.myntra.com')
read = BeautifulSoup(var.text, "lxml")
print(read)

NumberOfResults = read.select()
print(NumberOfResults)




