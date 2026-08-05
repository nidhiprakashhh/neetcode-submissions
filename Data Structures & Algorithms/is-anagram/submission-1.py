class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        smap = {}
        tmap = {}

        for let in s:
            if let not in smap:
                smap[let] = 1
            else:
                smap[let] += 1

        for let in t:
            if let not in tmap:
                tmap[let] = 1
            else:
                tmap[let] += 1

        for let in smap:
            if smap[let] != tmap.get(let, 0):
                return False
        
        return True


        