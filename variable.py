a = 10
b = "Hello"

print(type(a))
print(type(b))

a = True
print(type(a))

c, d, e, f = 10, 29, 39, 40
print(c, d, e, f)

g, h, i = "lee", "kim", "cho"
print(g, h, i)

str = "안녕하세요!!! '김태경' "
str_literal = '''
sdflkj\n
sdfldkj\n
sdflsk
dlfkd\n
djdj
'''

print(str)
print(str_literal)


# 주석처리
# 리터럴 표기방법

name = "김태경"
literal_1 = "안녕하세요!" + name +"그냥 써봄"

print(literal_1)

# 문자랑 숫자 섞어서 쓸 때, 앞에 f를 붙이면 변수를 자동적용가능
literal_2 = f"안녕하세요! {name}    그냥추가로써봄"
print(literal_2)