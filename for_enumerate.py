#enumerate 는 index생성시켜준다.
# _는 출력 생략 가능하게 해줌

for entry in enumerate(['A','B', 'C']):
    print(entry)

for i, data in enumerate(['A','B', 'C']):
    print(i)
    print(data)
    print('------------------')


for _ , data in enumerate(['A','B', 'C']):
    print(data)
    print('------------------')

for i, _ in enumerate(['A','B', 'C']):
    print(i)
    print('------------------')


# data_list = ["a", "b", "c"]
# for i in data_list:
#     print(f"{i} 헐")

for i, data in enumerate(['A','B','C']):
    print(f'{i}번째는 {data} 입니다.')

    print('{} 번째는 {}입니다'.format(i, data))