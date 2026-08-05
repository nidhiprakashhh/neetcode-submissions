class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}

        for i in range(0, len(s)):
            if s[i] in hashmap1:
                hashmap1[s[i]] += 1
            else:
                hashmap1[s[i]] = 1

        for i in range(0, len(t)):
            if t[i] in hashmap2:
                hashmap2[t[i]] +=1
            else:
                hashmap2[t[i]] = 1

        for i in range(len(s)):
            if s[i] not in hashmap2:
                return False
            
            if hashmap1[s[i]] != hashmap2[s[i]]:
                return False

        return True         
        