class Solution:
    def isPalindrome(self, s: str) -> bool:
        dup=""
        for i in s.lower():
            if i.isalnum():
                dup+=i
        rev=""
        for i in range(len(dup)-1,-1,-1):
            if dup[i].isalnum():
                rev+=dup[i]
        print ( rev)
        return rev==dup
        