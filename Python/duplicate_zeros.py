class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        """
            https://leetcode.com/submissions/detail/986299755/?from=explore&item_id=3245
            Leetcode: 3245
            Points to remember:
                - Sorted array
                - In-place operation
                - Utilize python's abilities32
        """
        idx = 0
        while idx < len(arr)-1:
            if arr[idx] == 0:
                arr.insert(idx+1, 0)
                # del arr[len(arr)-1] // O(n)
                arr.pop() 
                idx+=2
            else:
                idx+=1
