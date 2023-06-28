class Solution:
    # Main logic here to get the number of digits from the given number
    # Two ways
    
    # Approach 1:
    # Get the value with log10
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            num_digits = floor(log10(num)) + 1
            if num_digits % 2 == 0:
                result += 1
        return result

    # Approach 2:
    # Get the value with traditional way by diving number with 10 until it becomes zero

    # def getNumberOfDigits(self, num : int) -> int:
    #         count = 0
    #         while(num != 0):
    #             num //= 10
    #             count+=1
    #         return count
        
    # def findNumbers(self, nums: List[int]) -> int:
    #     result = 0
    #     for num in nums:
    #         if(self.getNumberOfDigits(num)%2 == 0):
    #             result+=1
    #     return result