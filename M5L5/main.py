class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language of India")

    def type(self):
        print("India is a developing country")

class America():
    def capital(self):
        print("Washington, D.C is the capital of America")

    def language(self):
        print("English is the primary language of America")

    def type(self):
        print("America ia a developed country")

obj_ind=India()
obj_America=America()
for country in (obj_America, obj_ind):
    country.capital()
    country.language()
    country.type()