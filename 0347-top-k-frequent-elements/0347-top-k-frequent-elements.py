class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[[] for i in range(len(nums)+1)]
        for i in nums:
            d[i]=1+d.get(i,0)
        for n,c in d.items():
            l[c].append(n)
        res=[]
        for i in range(len(l)-1,-1,-1):
            for j in l[i]:
                res.append(j)
                if len(res)==k:
                    return res
        
        