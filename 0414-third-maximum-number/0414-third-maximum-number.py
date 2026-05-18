class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=list(set(nums))
        if len(num)<3:
            return max(num)
        else:
            x=num.index(max(num))
            num.pop(x)
            x=num.index(max(num))
            num.pop(x)
            return max(num)


        