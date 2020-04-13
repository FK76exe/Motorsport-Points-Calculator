from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import bs4

def matrix_maker(url): #returns starting pos, driver names, and finish
    uClient = uReq(url) #opens connection and downloads page
    page_html = uClient.read() #reads file
    uClient.close() #closes connection
    page_soup = soup(page_html,"html.parser") #parses the html code
    cols = page_soup.findAll("table",{"class":"tb"})[2].findAll("td",{"class":['chasecol',"col"]}) #All the cells
    index = column_indexer(page_soup)[:4] #index of Fin,St,Driver,Led
    length = column_indexer(page_soup)[-1] #Index of length of column
    accumulator = [] #where results are stored
    for x in range(0,len(cols),length):
        info = [cols[x+index[0]].text,cols[x+index[1]].text,cols[x+index[2]].text.replace(' \xa0 ',''),cols[x+index[3]].text]
        accumulator.append(info)

    return accumulator
    #cols contains cell data, headers contain header data


def column_indexer(soup):
    headers = [] #headers
    for x in soup.find("tr",{"class":"newhead"}).findAll("th"):
        headers.append(x.text)
    driver_col,pos_col,qual_col,laps_col = -1,-1,-1,-1

    for h in range(len(headers)):
        if headers[h] == "Driver" and h < 11:
            driver_col = h
        elif headers[h] == "Fin":
            pos_col = h
        elif headers[h] == "St":
            qual_col = h
        elif headers[h] == "Led":
            led_col = h
    return (pos_col,qual_col,driver_col,led_col,len(headers))

def season_length(series,year):
    uClient = uReq("https://www.racing-reference.info/season-stats/{}/{}/".format(year,series))
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    num_races = [int(s) for s in page_soup.find("strong").text.split() if s.isdigit()]
    return num_races[0]


#print(matrix_maker("https://www.racing-reference.info/race?s=1&series=W&id=2016-27"))
#season_length("B",2011)


