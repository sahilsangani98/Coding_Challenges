class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Solution using set
        # Time complexity: O(n)
        # Space complexity: O(n
        """
            https://leetcode.com/problems/contains-duplicate/description/
            Leetcode: 217
            Points to remember:
                - Check for second occurence
                - Use set or dict property for uniqueness
        """

        setNums = set(nums)
        if len(setNums) == len(nums):
            return False
        else:
            return True