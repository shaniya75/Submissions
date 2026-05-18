class Solution:
    def kidsWithCandies(self, nums: List[int], n: int) -> List[bool]:
        res=[]
        for i in nums:
            if i+n>=max(nums):
                res.append(True)
            else:
                res.append(False)
        return res