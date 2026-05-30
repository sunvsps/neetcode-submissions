class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strSort = []
        for i in strs:
            strSort.append("".join(sorted(i)))
            

        setStrSort = set(strSort)

        #Add result
        result = []
        for i in setStrSort:
            r = []
            for j in range(0, len(strSort)):
                if i == strSort[j]:
                    r.append(strs[j])
            result.append(r)

        return result
        