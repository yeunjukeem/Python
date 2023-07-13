#func_lambda.py
#람다

# 람다 표현식에 조건부 표현식 사용하기
'''
람다 표현식에서 조건부 표현식을 사용하는 방법

lambda 매개변수들: 식1 if 조건식 else 식2
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list_data = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(list_data)

list_data_1 = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(list_data)


# map에 객체를 여러 개 넣기

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b))
[2, 8, 18, 32, 50]

# filter 사용하기

