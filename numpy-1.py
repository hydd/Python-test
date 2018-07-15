import numpy as np
# array = np.array([[1, 2, 3], [2, 3, 4]])
# print(array)
# print('number of dim:', array.ndim)
# print('shape:', array.shape)
# print('size:', array.size)

# a = np.array([[1, 2, 3], [2, 3, 4]], dtype=np.int)
# print(a)
# print(a.dtype)

# b = np.ones((3, 4), dtype=np.int16)
# print(b)

# c = np.empty((3, 4))
# print(c)

# d = np.arange(10, 20, 2)
# print(d)

# e = np.arange(12).reshape(3, 4)
# print(e)

# f = np.linspace(1, 10, 20)
# print(f)

# g = np.linspace(1, 10, 20).reshape(4, 5)
# print(g)

# h = np.array([10, 20, 30, 40])
# i = np.arange(4)
# print(h, i)
# print(h - i)
# print(h + i)
# print(h * i)
# print(i**2)
# c = 10 * np.sin(h)
# print(c)
# print(i, i < 3)

# a = np.array([[1, 2], [0, 1]])
# b = np.arange(4).reshape(2, 2)
# print(a, b)
# c = a * b
# c_doc = np.dot(a, b)
# c_doc_2 = a.dot(b)
# print(c)
# print(c_doc)
# print(c_doc_2)

# a = np.random.random((2, 4))
# print(a)
# print(np.sum(a, axis=0))
# print(np.min(a))
# print(np.max(a))

# A = np.arange(2, 14).reshape(3, 4)
# print(A)
# print(np.argmin(A)) # 最小
# print(np.argmax(A)) # 最大
# print(np.mean(A)) # 平均数
# print(A.mean())
# print(np.median(A)) # 中位数
# print(np.cumsum(A))  # 累加
# print(np.diff(A))  # 累差
# print(np.nonzero(A))  # 非零
# print(np.sort(A))  # 排序
# print(np.transpose(A))  # 转置
# print(np.clip(A, 5, 9))  # 范围外转换
# print(np.mean(A, axis=1))  # axis=1 行

A = np.arange(3, 15).reshape(3, 4)
print(A)
for row in A:
    print(row)
for column in A.T:
    print(column)
for item in A.flat:
    print(item, end=' ')
