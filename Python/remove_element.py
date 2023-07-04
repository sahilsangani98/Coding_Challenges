class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
            Leetcode: 3247
            Points to remember:
            - In place swap
            - Only consider first k elements and do not carry about last elements
            - Right pointer will be increased only for non target vals
        """
        
        rp = 0
        for idx in range(0, len(nums)):
            if nums[idx] != val:
                nums[rp] = nums[idx]
                rp+=1
        return rp