#cat_age_with_underscore.py

#캡슐화
#외부에서 수정 불가하게 전역변수 앞에 __를 붙이는 것.
class Cat:
    def __init__(self , name , age):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return f'Cat(name={self.__name} , age={self.__age}살)'
    
nabi = Cat("나비" , 10)
nero = Cat("네로" , 20)

print(nabi)
print("================================")
nabi.__age = 100
print(nabi)