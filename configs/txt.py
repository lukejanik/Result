import urllib.request as url
from Entry import Entry

#result_page = 'https://www.annapolisstriders.org/wp-content/uploads/2017/11/ColdTur2017-2017-Results.txt'
result_page = 'https://www.annapolisstriders.org/wp-content/uploads/2016/04/BAMar-Results-3.txt'
#result_page = 'http://www.mdtiming.com/2018/AS-Valentine2018Results.TXT'
table = [{}]

def findStart(lines):
    for line in lines:
        if "=" in line:
            return lines.index(line)
    return -1

def findRecognizedCol(col_name):
    name_list = ['Name', 'First', 'Last', 'name', 'NAME', 'FIRST', 'LAST']
    age_list = ['Ag', 'Age', 'age', 'AGE']
    gender_list = ['Sex', 'S', 'Gender']
    time_list = ['Gun Time', 'GunTime', 'Net Time', 'NetTime', 'Finish', 'Time', 'Gun', 'Chip', 'ChipTime']
    city_list = ['City', 'Town', 'City                 St']
    try:
        for name_option in name_list:
            if col_name.find(name_option) != -1:
                return 'Name'
        for age_option in age_list:
            if col_name.find(age_option) != -1:
                return 'Age'
        for gender_option in gender_list:
            if col_name.find(gender_option) != -1:
                return 'Gender'
        for time_option in time_list:
            if col_name.find(time_option) != -1:
                return 'Time'
        for city_option in city_list:
            if col_name.find(city_option) != -1:
                return 'City'
    except ValueError:
        return ''


def organizeTable(headers_line, indices):
    for i in range(0, len(indices) - 1):
        start_idx = indices[i]
        end_idx = indices[i+1]
        col_name = headers_line[start_idx:end_idx].strip()
        table.append({'ColName': col_name, 'StartIDX': start_idx, 'EndIDX': end_idx, 'RecName': findRecognizedCol(col_name)})
    for row in table:
        print(row)


def findIndices(equals_line):
    indices = []
    indices.append(0)
    for i in range(0, len(equals_line)):
        if equals_line[i] == " ":
            indices.append(i)
    return indices

data = url.urlopen(result_page)
lines = str(data.read()).split('\\r\\n')

equals_idx = findStart(lines)
headers_idx = equals_idx - 1

indices = findIndices(lines[equals_idx])
organizeTable(lines[headers_idx], indices)


entries = []
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





























