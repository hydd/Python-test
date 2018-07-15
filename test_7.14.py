list1 = [1, 2, 3, 4, 5, 6]
str1 = 'china'
for each in zip(list1, str1):
    print(each)

num = [[1, 1, 1], [1, 1, 1]]
num = list(set(tuple(n) for n in num))
num = [list(v) for v in num]
print(num)

num = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                num.append([i, j, k])
print(num)

i = int(input('请输入净利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        i = arr[idx]
print(r)
