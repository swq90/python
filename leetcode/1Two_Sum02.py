#排序，二分
def find_n( l, need):
    if (need > l[-1]['key'] )or(need < l[0]['key'] ):
        return
    n = int(len(l) / 2)
    x = l[n]
    if x['key'] < need :
        return find_n(l[n:], need)
    elif x['key'] > need:
        return find_n(l[:n], need)
    else:
        return l[n]['value']

def twoSum( nums, target) :
    l = []
    d = {}
    for i in range(len(nums)):
        d['key'] = nums[i]
        d['value'] = i
        d1 = d.copy()
        l.append(d1)
    l1 = sorted(l, key=lambda e: e['key'])

    for i in range(len(l1)-1):

        need = target-l1[i]['key']
        n=find_n(l1[i:],need)
        if n or n==0 :
            m=l1[i]['value']
            if m>n:
                return (n,m)
            else:
                return (m, n)

nums = [0,3,-3,4,-1]
target = -1
print(twoSum(nums,target))