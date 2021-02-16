# *first, last = [1, 2, 3, 5]
# print(sum(first), last)
# line = 'nobody:*:-2:-2:unprivileged user:/var/empyt:/usr/bin/false'
# uname, *field, homedir, sh = line.split(":")
# print(homedir)
# print(sh)
# print(field)
# print(uname)

#1.3
# from collections import deque
#
# def search(lines,pattern,history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line,previous_lines
#         previous_lines.append(line)
# # use on a file
# if __name__ == "__main__":
#     with open('somefile.txt ','r')as f:
#         for line,prevlines in search(f,"python",3):
#             for pline in prevlines:
#                 print(pline,end=" ")
#                 print("-"*20)


# # 1.4
# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))


# 1.6
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d['b'].append(4)
print(d['b'][1])
print(d['c'])

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

# A regular dictionary
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d['c'])
