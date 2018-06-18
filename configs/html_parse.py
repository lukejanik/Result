import json as j
import urllib.request as url
from bs4 import BeautifulSoup
from Entry import Entry

# print("1")
# data = url.urlopen("https://eventresults-api.sporthive.com/api/events/6375357357228396544/races/427167/classifications/search?count=10&offset=0").read()
# print("2")
# output = json.loads(data)

# rock n roll full
page = 'http://www.runrocknroll.com/finisher-zone/search-and-results/?resultspage=1&eventid=71&subevent_id=96245&yearid=&firstname=&lastname=&bib=&gender=&division=&state=&city=&perpage=1883'
# half
page = 'http://www.runrocknroll.com/finisher-zone/search-and-results/?resultspage=1&eventid=71&subevent_id=96242&yearid=&firstname=&lastname=&bib=&gender=&division=&state=&city=&perpage=10379'
# 5k
page = 'http://www.runrocknroll.com/finisher-zone/search-and-results/?resultspage=1&eventid=71&subevent_id=96244&yearid=&firstname=&lastname=&bib=&gender=&division=&state=&city=&perpage=1529'
# all
page = 'http://www.runrocknroll.com/finisher-zone/search-and-results/?resultspage=1&eventid=71&subevent_id=&yearid=&firstname=&lastname=&bib=&gender=&division=&state=&city=&perpage=13791'

entries = []

# Cherry pit
page = 'https://www.annapolisstriders.org/result/2018-cherry-pit-10-mile-race-results/'

# hat run 50k
page = 'https://ultrasignup.com/results_event.aspx?did=51102'

page = url.urlopen(page)
soup = BeautifulSoup(page, 'html.parser')
result = []

# self, name, gender, age, city, time

''' the following is for cherry pit 
body = soup.find_all('tbody')
result = body[0].find_all('tr')


for r in result:

    entry = r.find_all('td')
    new_entry = Entry(str(entry[1].text) + " " + str(entry[2].text), entry[4].text, entry[5].text, None, entry[3].text)
    entries.append(new_entry)
    '''

''' the following is for rock n roll
result = soup.find_all('tr')


for r in result:
    entry = r.find_all('td')
    if len(entry) > 2:
        name = entry[2].a.text
        time = entry[3].text
        new_entry = Entry(name, None, None, None, time)
        entries.append(new_entry)
'''

''' hat run 50k'''
print(soup)








