class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaString = ''
        for i in range(len(s)):
            if s[i].isalpha():
                alphaString += s[i]

        i = 0
        j = len(alphaString) - 1

        while (i < j):
            if alphaString[i] != alphaString[j]:
                return False
            i += 1
            j -= 1
        
        return True