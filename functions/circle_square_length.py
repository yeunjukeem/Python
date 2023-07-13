#circle_square_length.py

import math

##print 보다 return사용 권장
# return을 써야 추후의 데이터 활용이 가능하다.

def circle_square(a):
    square = a * a * math.pi
    length = 2*a * math.pi
   
    return square, length

a = int(input("반지름 길이: "))    

square, length = circle_square(a)
print(f'넓이는 {square}, 길이는 {length}')


#print ver.

def circle_square(a):
    square = a * a * math.pi
    length = 2*a * math.pi
    print(f'원의 넓이는 {square}')
    print(f'원의 지름은 {length}')
  
a = int(input("반지름 길이: "))    

