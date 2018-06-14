import json, urllib.request as url
from bs4 import BeautifulSoup
from Entry import Entry

data = url.urlopen("https://eventresults-api.sporthive.com/api/events/6375357357228396544/races/427167/classifications/search?count=1500&offset=0").read()
output = json.loads(data)

entries = []

page = url.urlopen('https://www.annapolisstriders.org/result/2018-cherry-pit-10-mile-race-results/')
soup = BeautifulSoup(page, 'html.parser')
result = []
body = soup.find_all('tbody')
result = body[0].find_all('tr')

for r in result:
    entry = r.find_all('td')
    new_entry = Entry(str(entry[1].text) + " " + str(entry[2].text), entry[4].text, entry[5].text, None, entry[3].text)
    entries.append(new_entry)

print(len(entries))

# results = result.split("tr")




# self, name, gender, age, city, time
'''
for result in output['fullClassifications']:
    entry = Entry(result['athlete']['name'], result['classification']['gender'], result['classification']['ageDuringEvent'],
                  None, result['classification']['gunTime'])
    entries.append(entry)
'''
for entry in entries:
    print(entry.__str__())

