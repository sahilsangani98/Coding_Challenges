class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(1)
        """
            https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
            Leetcode: 3251
            Points to remember:
                - All elements should be visited under two condition: Either increasing or decreasing
        """
        idx = 0
        # Increasing - Going to peak
        while(idx+1 < len(arr) and arr[idx] < arr[idx+1]):
            idx+=1
        
        # Invalid if Peak is 1st or last element
        # It covers condition for less than 3 given elements as an input
        if idx==0 or idx==len(arr)-1:
            return False
        
        # Decreasing 
        while(idx+1 < len(arr) and arr[idx] > arr[idx+1]):
            idx+=1
        
        # Returns true only if all elements seen with above condition
        return idx==len(arr)-1
