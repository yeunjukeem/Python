#cat_age_name_setter_getter.py

class Cat:
    def __init__(self, name="나비", age=3):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Cat Class : name = {self.__name}, age = {self.__age}'    

#  방법 1  ============================   
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
# 방법 2  ============================
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

print('''방법 1  ============================''')
cat = Cat("nero", 5)
print(cat)
# print(cat.__name)  #오류발생

print(cat.name)

cat.name = "미미"
print(cat.name)

print('''방법 2  ============================''')
print(cat.get_age()) 
cat.set_age(10)
print(cat.get_age())