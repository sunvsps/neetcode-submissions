class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            if mapS.get(s[i]) is None:
                mapS[s[i]] = 1
            else :
                mapS[s[i]] = mapS[s[i]] +1
            
            if mapT.get(t[i]) is None:
                mapT[t[i]] = 1
            else :
                mapT[t[i]] = mapT[t[i]] +1

        if len(mapS) != len(mapT):
            return False

        for i in mapS.keys():
            if mapS.get(i) != mapT.get(i):
                return False
        return True
