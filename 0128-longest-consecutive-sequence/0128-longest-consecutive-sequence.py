class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        store=set(nums)
        for i in store:
            if i-1 not in store:
                current = i
                streak=0
                while current in store:
                    current+=1
                    streak+=1
                    res=max(res,streak)
        return res
        