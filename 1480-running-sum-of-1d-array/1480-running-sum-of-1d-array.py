class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        op=[]
        sum=nums[0]
        op.append(sum)
        for i in range(1,len(nums)):
            sum+=nums[i]
            op.append(sum)
        return op
        