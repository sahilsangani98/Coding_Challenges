class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        LastMaxConsecNum = 0  # Remembers last Maximum Consecutive number
        CurrMaxConsecNum = 0  # Remembers current Maximum Consecutive number
        
        for idx in range(0, len(nums)):
            if nums[idx] == 1:
                CurrMaxConsecNum+=1
                # Check if Current Consecutive number is greater Last Consecutive number
                if CurrMaxConsecNum > LastMaxConsecNum:
                    LastMaxConsecNum = CurrMaxConsecNum
            else:
                # Reset Current Consecutive number
                CurrMaxConsecNum = 0
        
        return LastMaxConsecNum