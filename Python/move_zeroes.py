class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        # Time complexity: O(n)
        # Space complexity: O(1)
            https://leetcode.com/problems/move-zeroes/description/
            Leetcode: 283
            Points to remember:
                - Two pointers approach fast and slow pointer
                - Last remaining change to zeros
                - Another approach can be poping up element and append it to last element append/pop

        """
        sp, fp = 0, 0
        
        while(fp < len(nums)):
            if nums[fp] != 0:
                nums[sp] = nums[fp]
                sp+=1
                fp+=1
            else:
                fp+=1
        
        while (sp < len(nums)):
            nums[sp] = 0
            sp+=1