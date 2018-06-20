import urllib.request as url
from bs4 import BeautifulSoup
from Entry import Entry
import json as j

def main(pages, race):
    entries = []
    for page in pages:
        req = url.Request(page,  headers={'User-Agent': 'Mozilla/5.0'})
        result = url.urlopen(req)

        if race == "EC":
            all = j.load(result)
            results = all['items']
            for r in results:
                data = r['person']
                time = r['finalResult']['chipTimeResult']
                time = time[2:]
                name = data['firstName'] + " " + data['lastName']
                age = data['age']
                gender = data['gender']
                new_entry = Entry(name, gender, age, "", time)
                entries.append(new_entry)

        for entry in entries:
            print(entry)




# results = result.split("tr")

# cherry blossom
# https://eventresults-api.sporthive.com/api/events/6375357357228396544/races/427167/classifications/search?count=10&offset=0


# self, name, gender, age, city, time
'''
for result in output['fullClassifications']:
    entry = Entry(result['athlete']['name'], result['classification']['gender'], result['classification']['ageDuringEvent'],
                  None, result['classification']['gunTime'])
    entries.ap'''



