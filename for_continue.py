# 짝수만 더하기

sum = 0
for i in range(0,101,2):
    sum += i
print(sum)


#=================================

total_sum = 0
for num in range(1, 101):
    if num % 2 == 1:
        continue
    total_sum += num

print("짝수의 합:", total_sum)