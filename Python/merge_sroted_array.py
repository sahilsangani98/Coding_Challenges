class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
            https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
            Leetcode: 3253
            Points to remember:
                - Sorted array
                - In-place operation
                - Gurantee space for new elements
                - Do in reverse order
                - Don't forget left over elements if any
        """
        n1p = m + n -1
        
        # Reverse order merge
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]: # Compare both array's last element
                nums1[n1p] = nums1[m-1]
                m-=1
            else:
                nums1[n1p] = nums2[n-1]
                n-=1
            n1p-=1
        
        # remaining elements in num2 - Dump in num1
        while n > 0:
            nums1[n1p] = nums2[n-1]
            n-=1
            n1p-=1