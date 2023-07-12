class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.

        # Time complexity: O(2n)
        # Space complexity: O(1)
            https://leetcode.com/problems/product-of-array-except-self/description/
            Leetcode: 238
            Points to remember:
                - Figure out left side and right multplication form given index
                - Can use two arrays to get the value - Optimization: Traverse two times on same array
                - Keep record of pre and post multiplication number

        """
        pre = 1
        post = 1
        answer = [1]*len(nums)
        # Pre
        for idx in range(0, len(nums)):
            answer[idx] = pre
            pre = nums[idx] * pre
        # Post
        for idx in range(len(nums)-1, -1, -1):
            answer[idx] = answer[idx] * post
            post = nums[idx] * post
        return answer