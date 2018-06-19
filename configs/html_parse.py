import urllib.request as url
from bs4 import BeautifulSoup
from Entry import Entry

log = True


def main(pages, race):
    entries = []
    for page in pages:
        page = url.urlopen(page)
        print(page)
        soup = BeautifulSoup(page, 'html.parser')

        # self, name, gender, age, city, time
        if race == "Cherry Pit":
            body = soup.find_all('tbody')
            result = body[0].find_all('tr')

            for r in result:
                entry = r.find_all('td')
                new_entry = Entry(str(entry[1].text) + " " + str(entry[2].text), entry[4].text, entry[5].text, None, entry[3].text)
                entries.append(new_entry)

        if race == "Rock n Roll":
            result = soup.find_all('tr')

            for r in result:
                entry = r.find_all('td')
                if len(entry) > 2:
                    name = entry[2].a.text
                    time = entry[3].text
                    new_entry = Entry(name, None, None, None, time)
                    entries.append(new_entry)

        if race == "Shamrock":
            body = soup.find_all('tbody')
            result = body[0].find_all('tr')
            for r in result:
                entry = r.find_all('td')
                if len(entry) >= 7:
                    name = entry[1].text.strip() + " " + entry[2].text.strip()
                    city = entry[3].text.strip()
                    age = entry[5].text.strip()
                    gender = entry[6].text.split()[1].strip()
                    time = entry[7].text.strip()
                    entries.append(Entry(name, gender, age, city, time))

        if race == "Germantown":
            print("HI!")
            body = soup.find_all('tbody')
            result = body[0].find_all('tr')
            print(result)
            for entry in result:
                if len(entry) >= 6:
                    name = entry[4].text.strip()
                    print(name)


        if log:
            for entry in entries:
                print(entry)










