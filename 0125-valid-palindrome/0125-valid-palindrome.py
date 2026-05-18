class Solution:
    def isPalindrome(self, s: str) -> bool:
        dup=""
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                dup+=i
        rev=""
        for i in range(len(dup)-1,-1,-1):
            if dup[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                rev+=dup[i]
        print ( rev)
        return rev==dup
        