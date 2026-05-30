class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
            
        cond = ['(', ')', '[', ']', '{', '}']
            
        l = []
        for i in s:
            l.append(i)
            
        i = 0
        minus = 1

        while i < len(l) - minus:
            indexFind = cond.index(l[i])
            find = ""
            if indexFind % 2 == 0:
                find = cond[indexFind+1]
            else:
                l.pop(i)
                continue
            flag = True
            for j in range(1,len(l)):
                if l[j] == find and j % 2 == 1:
                    l.pop(j)
                    l.pop(i)
                    flag = False
                    break
            if flag :
                minus = minus + 1
        if len(l) == 0:
            return True
        return False