#func_arguments.py

# a, b, c 매개변수
def multiple_add(a, b, c):
    num = a*b+c
    return num
a = 2
b = 3
c = 4

# a, b, c 위치인자로 전달
result = multiple_add(2, 3, 4)
print(result)

#a, b, c를 키워드 인자로 전달
# 키워드 인자 keyword arguments: 매개변수에서 쓴 매개변수명 그대로 사용!!

result_keywords = multiple_add(2, 3, 4)
print(result_keywords)


# 키워드 인자는 위치를 바꿔도 된다.
result_keywords_1 = multiple_add(a=2, c=4, b=3)
print(result_keywords_1)

# error! positional arguments follows keyword argument
#(위치인자, 키워드인자 섞어서 쓰는 경우): 위치인자는 키워드인자 다음으로 온다.
#위치인자부터 부터 먼저 호출하고 나중에 키워드 인자를 나열한다.

result_keywords_1 = multiple_add(2, 3, c=4)
print(result_keywords_1)

#매개변수 키워드값을 부여하면 인자값으로 전달 받지 않아도 된다.
#매개변수에 기본값을 지정해두면, 다시 입력하지 않아도 된다.
def multiple_add_keywords(a, b, c=100):
    num = a*b+c
    return num
result_1 = multiple_add_keywords(10,20)
print(result_1)
# 물론! 바꿔도 된다
result_2 = multiple_add_keywords(10,20, 500)
print(result_2)
#
result_2 = multiple_add_keywords(a=10,b=20, 500)
print(result_2)