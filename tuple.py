t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1, 2, 3
t5 = ('a','b',('ab','cd'))

print(t5[0])
print(t5[2][1])


#indexing
t1 = (1, 2, 'a', 'b')
print(t1[0])

#slicing

t1 = (1, 2, 'a', 'b','c')
print(t1[1:])
print(t1[-3:])
print(t1[:-1])
print(t1[:1])


#원소의 개수
print(len(t1))

for i in range(len(t1)):
    print("hello")

# print("Hello" * len(t1))



#tuple 더하기

t2 = (3, 4)
t3 = t1 + t2

print(t3)

t4 = t1 * 3
print(t4)


# print(tuple(1,)) 
print(tuple([1,2,3]))
