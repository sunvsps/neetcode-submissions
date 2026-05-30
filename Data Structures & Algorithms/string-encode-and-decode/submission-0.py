class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            asciiL = ""
            for j in i:
                asciiL = asciiL + str(ord(j)) + ";"
            res = res + asciiL + "&"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        fullString = ""
        ss = ""
        for i in s:
            if i == ";":
                fullString = fullString + chr(int(ss))
                ss = ""
            elif i == "&":
                res.append(fullString)
                fullString = ""
            else:
                ss = ss + i
        return res

