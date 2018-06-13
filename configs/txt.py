import urllib.request as url
from Entry import Entry

result_page = 'https://www.annapolisstriders.org/wp-content/uploads/2017/11/ColdTur2017-2017-Results.txt'
table = [{}]

def findStart(lines):
    for line in lines:
        if "Place" in line:
            return lines.index(line)
    return -1

def findRecognizedCol(col_name):
    name_list = ['Name', 'First', 'Last', 'name', 'NAME', 'FIRST', 'LAST']
    age_list = ['Ag', 'Age', 'age', 'AGE']
    gender_list = ['Sex', 'S', 'Gender']
    time_list = ['Time', 'Gun Time', 'GunTime', 'Net Time', 'NetTime', 'Finish']
    city_list = ['City', 'Town']
    try:
        if col_name in name_list:
            return 'Name'
        elif col_name in age_list:
            return 'Age'
        elif col_name in gender_list:
            return 'Gender'
        elif col_name in time_list:
            return 'Time'
        elif col_name in city_list:
            return 'City'
    except ValueError:
        return ''


def organizeTable(first):
    first_split = first.split()
    for col_name in first_split:
        start_idx = first.find(col_name)
        try:
            end_idx = first.find(first_split[first_split.index(col_name) + 1])
        except:
            end_idx = len(first) - 1

        table.append({'ColName': col_name, 'StartIDX': start_idx, 'EndIDX': end_idx, 'RecName': findRecognizedCol(col_name)})


data = url.urlopen(result_page)
lines = str(data.read()).split('\\r\\n')
first = lines[findStart(lines)]
organizeTable(first)
entries = []

attributes = ['Name', 'Age', 'Gender', 'City', 'Time']

results = lines[findStart(lines) + 2:]
for result in results:
    name = ''
    age = ''
    city = ''
    gender = ''
    time = ''
    for row in table:
        if row.get('RecName') == 'Name':
            s = row.get('StartIDX')
            e = row.get('EndIDX')
            name = result[s:e]
        elif row.get('RecName') == 'Age':
            s = row.get('StartIDX')
            e = row.get('EndIDX')
            age = result[s:e]
        elif row.get('RecName') == 'Gender':
            s = row.get('StartIDX')
            e = row.get('EndIDX')
            gender = result[s:e]
        elif row.get('RecName') == 'City':
            s = row.get('StartIDX')
            e = row.get('EndIDX')
            city = result[s:e]
        elif row.get('RecName') == 'Time':
            s = row.get('StartIDX')
            e = row.get('EndIDX')
            time = result[s:e]
    entry = Entry(name, gender, age, city, time)
    entries.append(entry)

for entry in entries:
    print(entry)





























