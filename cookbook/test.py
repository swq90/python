# *first, last = [1, 2, 3, 5]
# print(sum(first), last)
# line = 'nobody:*:-2:-2:unprivileged user:/var/empyt:/usr/bin/false'
# uname, *field, homedir, sh = line.split(":")
# print(homedir)
# print(sh)
# print(field)
# print(uname)

#1.3
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

