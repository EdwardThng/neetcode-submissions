class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaString = ''
        for i in range(len(s)):
            if s[i].isalnum():
                alphaString += s[i]

        i = 0
        j = len(alphaString) - 1

        while (i <= j):
            front = alphaString[i].lower()
            back = alphaString[j].lower()
            if front != back:
                return False
            i += 1
            j -= 1
        
        return True