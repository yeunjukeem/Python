# class_inheritance.py


# 클래스 상속

#클래스 모두에 __init__()이 있으면, 
# 상속받고자 하는 attribute를 가지고 오는 식을 자식클래스에 super()를 사용

class Family:
    def __init__(self):
        self.lastname = "김"
    def lname(self):
        print(f'성은 {self.lastname}')

 
class Person(Family):

    def __init__(self):
        super().__init__() ##이거 추가!!
        self.firstname = "태경"
    def fname(self):
        print(f'이름은 {self.firstname}')

    
family = Family()
person = Person()
family.lname()
person.fname()



print(person.lastname)