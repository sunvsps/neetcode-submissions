class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        setNums = set(nums)
        countL = []

        for i in setNums:
            count = nums.count(i)
            countL.append([count,i])

        
        countL.sort()
        print(countL)
        result = []

        while len(result) < k:
            result.append(countL.pop()[1])
        return result
        