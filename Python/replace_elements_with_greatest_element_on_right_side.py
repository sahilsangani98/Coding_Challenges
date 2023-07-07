class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
            https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
            Leetcode: 3259
            Points to remember:
                - Iterate from last as we know last value
                - Keep record of greatest value
        """
        greatestVal = -1
        for idx in range(len(arr)-1, -1, -1):
            if arr[idx] > greatestVal:
                arr[idx], greatestVal = greatestVal, arr[idx] # Swap values
            else:
                arr[idx] = greatestVal
        return arr