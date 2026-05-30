class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        med = start + end // 2

        while start <= end:
            med = (start + end) // 2
            print(med, start, end)
            if med >= len(nums):
                break
            elif nums[med] == target:
                return med
            elif nums[med] < target:
                # print("start", nums[med], target)
                start = med + 1
            elif nums[med] > target:
                # print("end", nums[med], target)
                end = med - 1
        
        return -1
        