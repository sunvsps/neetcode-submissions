class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height)-1

        leftMax = height[L]
        rightMax = height[R]
        total = 0

        while L < R:

            if height[L] < height[R]:

                #update leftMax
                if leftMax < height[L]:
                    leftMax = height[L]

                if height[L] < leftMax:
                    total += leftMax - height[L]

                L+=1

            else:

                #update rightMax
                if rightMax < height[R]:
                    rightMax = height[R]

                if height[R] < rightMax:
                    total += rightMax - height[R]

                R-=1
        
        return total

