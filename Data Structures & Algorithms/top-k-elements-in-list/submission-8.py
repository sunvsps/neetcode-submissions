class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            #remove fequent
            l = []
            fequent = []
            maxF = 0
            for i in nums:
                if not self.containNum(l, i):
                    l = self.addNumber(l, i)          

            countl= [0] * len(l)  

            #Find Max
            for i in range(len(l)):
                count = 0
                for j in range (len(nums)):
                    if l[i] == nums[j]:
                        count = count + 1
                countl[i] = count
                if maxF < count:
                    maxF = count

            while len(fequent) < k:
                for i in range(len(countl)):
                    if countl[i] == maxF:
                        fequent = self.addNumber(fequent, l[i])
                maxF = maxF - 1

            return fequent


    def addNumber(self, l, num):
        size = len(l)
        # print("size", size)
        l1= [0] * (size+1)
        for i in range(len(l)):
            l1[i] = l[i]

        l1[size] = num
        return l1


    def containNum(self, l, number):
        for i in l:
            if i == number:
                return True

        return False


