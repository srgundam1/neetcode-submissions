class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s) - 1
        while i < j:
            while(not(s[i].isalnum()) and i < j):
                i += 1
                continue
            while(not(s[j].isalnum()) and j > i):
                j -= 1
                continue
            if (s[i].lower()!=s[j].lower()):
                return False
            i+=1
            j-=1
        return True