from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import csv

wanggu = "https://www.wantgoo.com/stock/astock/agentstat2?stockno=2329"

class webclaw():
    def __init__(self,path):
        self.path = path
        self.soup = None

    def readpage(self):
        driver = webdriver.PhantomJS(executable_path="D:\\phantoMJS\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
        driver.get(self.path)
        pagesource = driver.page_source
        self.soup = BeautifulSoup(pagesource, 'lxml')
        return self.soup

num = open('stockcode.csv','r')
rows = list(num)
stockcode = []
for i in range(len(rows)):
    stockcode.append(''.join(list(filter(str.isdigit, rows[i]))))



# WG = webclaw(path=wanggu).readpage()
# table = WG.find(id = 'listResult').find_all('tr')
# for i in range(1,len(table)):
#     tr = table[i]
#     td = tr.findAll('td')
#     date = td[0].contents[0]
#     bsdiff = td[3].contents[0]
#     # print(td[0].contents[0] + '\t' + td[3].contents[0]+ '\n')





