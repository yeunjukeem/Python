# class_inheritance_without_childclass_init.py

# 클래스 상속

# 자식 클래스 __init__()이 없으면, 
# 부모클래서에 있는 모든 속성을 사용가능.
#  자식클래스에 super()를 사용할 필요가 없음!!

class Family:
    def __init__(self):
        self.lastname = "김"
    def lname(self):
        print(f'성은 {self.lastname}')

 
class Person(Family):

    
    self.firstname = "태경"
    def fname(self):
        print(f'이름은 {self.firstname}')

    
family = Family()
person = Person()
family.lname()
person.fname()



print(person.lastname)