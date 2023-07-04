class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
            Leetcode: 3248
            Points to remember:
            - Same as remove element problem
            - Take advantage of sorted array and remember last unique value until you find new one
        """
        rp = 0
        lastUnique = None # Taken None as a value because input range is -ve to +ve
        for idx in range(0, len(nums)):
            if nums[idx] != lastUnique:
                nums[rp] = nums[idx]
                lastUnique = nums[idx]
                rp+=1
        return rp
        