
#dict
# immutable 예 ;변경이 불가능-
# key값에는 문자, 숫자, 튜플, 불린 가능

a = {1: 5, 2: 3}   # int 사용
print(a)
{1: 5, 2: 3}
a = {(1,5): 5, (3,3): 3} # tuple사용
print(a)
{(1, 5): 5, (3, 3): 3}
a = { 3.6: 5, "abc": 3} # float 사용
print(a)
{3.6: 5, 'abc': 3}
a = { True: 5, "abc": 3} # bool 사용
print(a)
{True: 5, 'abc': 3}

# mutable 예
# a = { {1, 3}: 5, {3,5}: 3}     #set 사용 에러
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'set'
# a = {[1,3]: 5, [3,5]: 3}     #list 사용 에러
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# a = { {"a":1}: 5, "abc": 3}     #dict 사용 에러
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'dict'


#값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워집니다.
{"a" : 1, "a":2}
{'a': 2}

print({"a" : 1, "a":2})

# print(a2[(1,5)])

#keys, values(), items()
print(a.keys())
print(a.values())
print(a.items())


#dict 만들기

result = dict([('a',1),('b',2),("c",3)])
print(result)

# 새로운 키와 값을 아래와 같이 추가할 수 있습니다.
d = {'abc': 1, 'def': 2}
d['키값'] = 10
print(d)


#dict 만들기

newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
print(newdict)
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}


# dictionary(딕셔너리) 변환
# 리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 
# 키와 value를 나란히 입력하면, 아래와 같이 dict로 변형할 수 있습니다.

name_and_ages = [['alice', 5], ['Bob', 13]]
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = [('alice', 5), ('Bob', 13)]
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = (('alice', 5), ('Bob', 13))
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = (['alice', 5], ['Bob', 13])
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}

#여러값 수정- update() 
# 키가 있는 값은 수정,키가 없는 값이면 추가
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
a.update({'bob':99, 'tony':99, 'kim': 30})
print(a)
{'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}


# dictionary(딕셔너리) for문
# for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
# 순서는 임의적이다.같은 순서를 보장할 수 없다.

a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for key in a:
    print(key)

# value값으로 for문을 반복하기 위해서는 values() 를 사용
for val in a.values():
    print(val)

# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for i in a.items():
    print(i)

    key_list=[]
    value_list=[]

for key, value in a.itmes():
    key_list.append(key)
    value_list.append(value)

print(key_list)
print(value_list)

# dictionary(딕셔너리) 의 in :key 에 한해서 동작
# --> value에서 찾으려면, value 리스트를 만들어서 그 안에서 찾기
print('alice' in a)
'teacher' in a

