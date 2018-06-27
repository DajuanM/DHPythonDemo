# zip
l1 = [1,2,3,4]
l2 = [10,20,30,40]
z = zip(l1,l2)
print([i for i in z])

# enumerate
l = [10,20,30,40]
em = enumerate(l)
l2 = [i for i in em]
print(l2)

em = enumerate(l, start=100)
l2 = [i for i in em]
print(l2)

# collections模块
# - nametuple
# - deque 解决了频繁删除插入的效率问题
import  collections
Point = collections.namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y, p[0], p[1])
print(isinstance(p, tuple))

from collections import deque
q = deque([1,2,3,4])
print(q)
q.append(5)
print(q)
q.appendleft(0)
print(q)

# defaultdict
from collections import defaultdict
d = {"a": 1, "b": 2, "c": 3}
print(d["a"])

func = lambda: "默认值"
d = defaultdict(func)
print(d["a"])

# Counter 统计字符串个数
from collections import Counter
c = Counter("as;mdoqwoingqwoiepoqwmdoqwnokwqndqw")
print(c)
s = ["1", "2", "2", "3", "3", "3"]
c = Counter(s)
print(c)




