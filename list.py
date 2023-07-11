a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ('Life', 'is')]


#중첩된 리스트에서 슬라이싱하기
f = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(f[2:5])
print(f[3][:2])

#리스트 더하기
print(a + b)

#리스트 곱하기

#리스트 수정과 삭제
#수정

z = [1, 2, 3]
z[2] = 10
print(z)

# del 함수를 사용해서 리스트 요소 삭제

del z[1]
print(z)

# del z[2]


#리스트 요소 제거-remove
y = [1, 2, 3, 1, 2, 3]
y.remove(3)
print(y)



#리스트 요소 끄집어 내서 삭제 -pop

q = [1, 2, "ㅁ"]
q.pop()
print(q.pop())
print(q)

#리스트에 요소 추가하기 - append
# 맨 마지막에 요소 추가됨

q.append(4)
print(q)


#리스트에 요소 추가하기 - insert
#원하는 인덱싱 위치에 추가
# insert(a,b)는 리스트의 a번째 위치에 b를 삽입하는 함수
t =[1, 2, 3]
t.insert(0,4)
print(t)

#extend()
nums = [1, 2, 3, 4]
nums.extend(['a','b'])
print(nums)

# sort(*, key=None, reverse=False)
# sorted(iterable, /, *, key=None, reverse=False)

a = ["b", "a"]
b = [5, 2, 3, 1, 4]
c = sorted(["b", "a"])
a.sort()
b.sort()
print(a)
print(b)
print(c)


a.sort(reverse=True)
# d.sort(b, reverse=True)
print(a)
b.sort(reverse=True)
print(b)
print(c)


# key
# 정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
# key 값을 기준으로 정렬되고 기본값은 오름차순이다

str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))

#리스트뒤집기 -reverse
# 크기비교 없이 요소의 배열을 뒤집어줌

a = ['a', 'c', 'b']
f = [1, 2, 'a', 'c', 'b']
a.reverse()
print(a)
f.reverse()
print(f)
# g.reverse()
# print(g)

#인덱스 변환 -index
a = [1,2,3]
a.index(3)
print(a)


# count 함수
# 변수.count(찾는 요소)
a = [1,1,1,2,3]
print(a.count(1))

#clear

a = [1,1,1,2,3]
a.clear()
print(a)

a.append(5)
print(a)

a.extend([3,4])
print(a)

a.append([3,4])
print(a)