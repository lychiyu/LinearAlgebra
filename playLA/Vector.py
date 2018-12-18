import math

from playLA._global import EPSILON


class Vector:
    def __init__(self, l):
        """使用列表初始化向量"""
        self._values = list(l)

    def __repr__(self):
        return f"Vector({self._values})"

    def __str__(self):
        return f"({', '.join(str(e) for e in self._values)})"

    def __len__(self):
        """向量维度"""
        return len(self._values)

    def __getitem__(self, item):
        """取出值"""
        if item < len(self):
            return self._values[item]
        return None

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __add__(self, other):
        """向量加法"""
        assert len(self) == len(other), '向量相加时维度必须相同'
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法"""
        assert len(self) == len(other), '向量相减时维度必须相同'
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """向量数乘"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """向量右乘,就是向量数乘"""
        return self * k

    def __pos__(self):
        """向量取正的结果"""
        return 1 * self

    def __neg__(self):
        """向量取负的结果"""
        return -1 * self

    def __truediv__(self, k):
        """返回数量除法的结果向量"""
        return 1 / k * self

    @classmethod
    def zero(cls, dim):
        """返回dim维零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        """归一化:返回向量的单位向量"""
        if self.norm() < EPSILON:
            raise ZeroDivisionError('向量的模是0')
        return Vector(self._values) / self.norm()

    def dot(self, other):
        """向量点乘，返回一个标量"""
        assert len(self) == len(other), '向量点乘时维度必须相同'
        return sum(a * b for a, b in zip(self, other))
