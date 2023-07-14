# class_inheritance_error.py

# 클래스 상속
# 아들은 아빠 속성 사용가능
# BUT 아빠는 아들 속성 사용 못함!!!
class Family:
    lastname = '김'
    def lname(self):
        print(f'성은 {Family.lastname} ')

class Person(Family):
    firstname = "태경"
    def fname(self):
        print(f'이름은 {self.firstname} 입니다.')

family = Family()
person = Person()
family.lname()
person.fname()

person.lname()


# 아래는 오류를 잘 보자
print(person.lastname)