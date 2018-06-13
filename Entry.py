class Entry(object):
    def __init__(self, name, gender, age, city, time):
        self.name = str(name)
        self.gender = str(gender)
        self.age = str(age)
        self.city = str(city)
        self.time = str(time)

    def __str__(self):
        return "Name: " + self.name + "\nGender: " + self.gender + "\nAge: " + self.age + \
               "\nCity: " + self.city + "\nTime: " + self.time + "\n"

