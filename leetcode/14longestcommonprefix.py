class Solution:
    def longestCommonPrefix1(self, strs) -> str:

        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if prefix == "":
                    return prefix
        return prefix

from solution import Solution
strs =['flow','flower','fly']
print(strs.longestCommonPrefix1())

# #from discuss
#     def longestCommonPrefix2(self, strs: List[str]) -> str:
#         sc,prefix = zip(*strs),""
#         for i in sc:
#             if(len(set(i)) !=1):
#                 break
#             prefix += i[0]
#         return  prefix
