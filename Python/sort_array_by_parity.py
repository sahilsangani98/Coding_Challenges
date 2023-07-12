class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        # Time complexity: O(n)
        # Space complexity: O(1) (Inplace operatiom)
            https://leetcode.com/problems/sort-array-by-parity/description/
            Leetcode: 905
            Points to remember:
                - two pointer approach
                - one pointer for even number and other one for odd number increase only while found
                - Swap numbers if it's odd ()

        """
        i, j = 0, len(nums)-1

        while i < j:
            if nums[i]%2 > nums[j]%2:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i]%2 == 0:
                i+=1
            if nums[i]%2 == 1:
                j-=1
        return nums
        