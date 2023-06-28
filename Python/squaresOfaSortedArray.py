class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two pointer approach
        # Advantage of 'Non-decreasing' array in given list
        # Most max number will be either square of left most number or right most number
        # Check for the condition and add to the max to min order

        arrSize = len(nums)
        leftPointer = 0
        rightPointer = arrSize - 1
        result = [0]*arrSize
        for idx in range(arrSize - 1, -1, -1):
            if(abs(nums[leftPointer]) > abs(nums[rightPointer])):
                squaredNum = nums[leftPointer]
                leftPointer+=1
            else:
                squaredNum = nums[rightPointer]
                rightPointer-=1
            result[idx] = squaredNum**2
        return result