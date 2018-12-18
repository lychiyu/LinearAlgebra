import numpy as np

if __name__ == '__main__':
    print(np.__version__)
    # numpy创建array 向量
    vec1 = np.array([1, 2, 3])
    print(vec1)
    zero_vec = np.zeros(5)
    # 默认是浮点型
    print(zero_vec)  # [0. 0. 0. 0. 0.]
    print(np.ones(5))  # [1. 1. 1. 1. 1.]
    print(np.full(5, 666))  # [666 666 666 666 666]

    # numpy.array的基本属性
    print(vec1.size)
    print(len(vec1))
    print(vec1[0], vec1[-1])
    print(vec1[:2])
    print(type(vec1[:2]))  # <class 'numpy.ndarray'>

    # numpy.array的基本计算
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])
    print(vec1 + vec2)
    print(vec1 - vec2)
    print(vec1 * 3)  # 向量数乘
    print(vec1.dot(vec2))  # 向量点乘
    print(np.linalg.norm(vec2))  # 向量的模
    print(vec2 / np.linalg.norm(vec2))  # 向量的单位向量
    print(np.linalg.norm(vec2 / np.linalg.norm(vec2)))
