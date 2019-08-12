from collections import namedtuple
point=namedtuple('point',('x','y'))
p=point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,point))
print(isinstance(p,tuple))
circle=namedtuple('circle',('x','y','r'))
c=circle(1,2,3)
print((c.x,c.y,c.r))
# 方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便

from collections import deque
q=deque(['a','b','c'])
print(q)
q.append('x')
print(q)
q.appendleft('A')
print(q)
q.pop()
print(q)
q.popleft()#头部删除
print(q)

#defaultdict ,如果key不存在返回默认值
from collections import defaultdict
dd=defaultdict(lambda : 'hh')
dd['key1']='kk'
print(dd['key2'])

#
