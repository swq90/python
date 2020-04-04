class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums):
        self.create_state_space_tree(nums, [], 0, [0 for i in range(len(nums))])
        return self.res
    
    def create_state_space_tree(self,sequence, current_sequence, index, index_used):
        if index==len(sequence):
            print(current_sequence)
            self.res.append(current_sequence.copy())
            return
        for i in range(len(sequence)):
            if not index_used[i]:
                current_sequence.append(sequence[i])
                index_used[i]=True
                self.create_state_space_tree(sequence,current_sequence,index+1,index_used)
                current_sequence.pop()
                index_used[i]=False

o=Solution()
z=o.permute([1,3,2,5])
print(z)