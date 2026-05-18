class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[0:n]
        y=nums[n:len(nums)]
        res=[]
        for i in range(len(x)):
            res.append(x[i])
            res.append(y[i])
        return res
        