#数据结构和算法
##1.1 将序列分解为单独的变量
任何可迭代的对象都可以通过 赋值来分解为单独的变量，字符串、文件、迭代器、生成器
```python
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ] 
name, shares, price, date = data 
# _, shares, price, _ = data

```
##1.2 从任意长度可迭代的对象中分解元素
*表达式，可以位于列表的任意位置，*变量名解压出来的变量永远使列表类型，无论
用于分解未知或任意长度的可迭代对象
1. *在迭代元素是可变长的元组序列
2. 星号解压，字符串操作，eg：字符串分割
3. 如果要分解后丢弃，*加常用变量名：_或者ign（ignored）
4. *分解操作和 列表处理功能相似（比如递归）
```python
# 和特定字符串处理操作结合，字符串分割
line = 'nobody:*:-2:-2:unprivileged user:/var/empyt:/usr/bin/false'
uname,*field,homedir,sh = line.split(":")
```
##1.3 保存最后N个元素
保存有限历史记录，collections.deque
我们在写查询元素的代码时，通常会使用包含 yield 表达式的生成器函数
使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。队列已满加入新元素时，最老的元素将会被移除
```python
from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)
# use on a file
if __name__ == "__main__":
    with open('somefile.txt ','r')as f:
        for line,prevlines in search(f,"python",3):
            for pline in prevlines:
                print(pline,end=" ")
                print("-"*20)
```

##1.4 找到最大或最小的N个元素
heapq模块有两个函数： nlargest() 和 nsmallest() 可以完美解决这个问题。
```python
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
cheap = heapq.nsmallest(3,portfolio,key=lambda s:s["price"])
expensive = heapq.nlargest(3,portfolio,key=lambda s:s["price"])
# 集合进行堆排序
heapq.heapify(nums)
#pop先将第一个元素弹出
heapq.heappop(nums)

```
如果想找唯一的极值，max,min更快；如果N的大小和集合大小相近，排序后切片更快sorted(items)[:N],sorted(items)[-N:],在正确的场合选择核实的方法
##1.5 实现优先级队列
```python

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
q.pop()
# 
# Item('bar')
# Item('spam')
# Item('foo')
# Item('grok')
# pop()返回优先级最高的，优先级相同，则按插入顺序
```
heapq.heappush(),heapq.heappop(),分别在_queue上插入和删除一个元素，保证第一个元素拥有最小优先级，heappop()总是返回“最小”的元素，保证pop返回正确元素，push pop实践复杂度O(N),N是堆的大小，
(-priority, self._index, item)元组，优先级为负是为了使元素按照优先级高到低排序，和按优先级从低祷告排序相反
index变量保证同优先级元素正确排序，确保他们插入的顺序
##1.6 在字典中将键映射到多个值上
```python
d = {'a':[1, 2, 3],'b':[4, 6]}
d = {'a':{1, 2, 3},'b':{4, 6}}
```
**collections.defaultdict**
```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
```
defaultdict 会自动为将要访问的键(就算目前字典中并不存在这样的键) 创建映射实体。 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。
```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d['c'])
#输出 []

# A regular dictionary
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d['c'])
#keyerror,报错
```

初始化，与数据处理中记录归类有关，1.15
```
from collections import defaultdict

d = {} 
for key, value in pairs:    
    if key not in d:        
        d[key] = []    
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:   
    d[key].append(value)
```

##1.7 让字典保持有序
##1.8 与字典有关的计算问题
##1.9 在两个字典中寻找相同点
##1.10 从序列中移除重复项且保持元素间顺序不变
##1.11 对切片命名
##1.12 找出序列中出现次数最多的元素
##1.13 通过对公共键对字典列表排序
##1.14 对不原生支持比较操作的对象排序
##1.15 更加字段将记录分组
##1.16 筛选序列中的元素
##1.17 从字典中提取子集
##1.18 将名称映射到序列的元素中
##1.19 同时对数据做转换和换算
##1.20 将多个映射合并为单个映射


##############################################################################################################