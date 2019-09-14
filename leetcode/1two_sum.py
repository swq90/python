#twoSum 哈希，快90%

# def twoSum1(nums):
#     l = []
#     d = {}
#     for i in range(len(nums)):
#         d[nums[i]] = i
#         # d1 = d.copy()
#         # l.append(d1)
#     print(d)
# nums = [3,2,4]
# print(twoSum1(nums))
class Solution:
    def twoSum( nums, target) :
        # l = []
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        # l1 = sorted(l, key=lambda e: e['key'])
        # for i in range(len(l1)-1):
        # nums.sort()
        # print(nums)
        for i in range(len(nums)-1):
            need = target-nums[i]
            if  (need in d) and (d[need]>i):
                return [i,d[need]]

#排序，二分
    def find_n(self,l, need):
        if (need > l[-1]['key'] )or(need < l[0]['key'] ):
            return
        n = int(len(l) / 2)
        x = l[n]
        if x['key'] < need :
            return self.find_n(l[n:], need)
        elif x['key'] > need:
            return self.find_n(l[:n], need)
        else:
            return l[n]['value']


    def twoSum2(nums, target, find_n=None):
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
            n = find_n(l1[i:],need)
            if n or n == 0:
                m = l1[i]['value']
                if m > n:
                    return (n, m)
                else:
                    return (m, n)
