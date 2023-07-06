class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Solution using set
        # Time complexity: O(n)
        # Space complexity: O(n)
        """
            https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
            Leetcode: 3250
            Points to remember:
                - Track seen numbers
                - Number's double's existance can come into picture in future as well - Handle it
                - Other way: Add both double and half value as seen value - Space Complexity O(n)*2
        """
        seenValSet = set()
        for idx in range(0, len(arr)):
            if arr[idx]*2 in seenValSet or arr[idx] % 2 == 0 and arr[idx] // 2 in seenValSet:
                return True
            else:
                seenValSet.add(arr[idx])
            