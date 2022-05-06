class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        if len(B) < len(A):
            A, B = B, A
        total = len(A) + len(B)
        H = total // 2
        left = 0
        right = len(A) - 1
        
        while True:
            i = (left + right) // 2
            j = H - i - 2
            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = float('-inf')
            if i + 1 < len(A):
                Aright = A[i + 1]
            else:
                Aright = float('inf')
            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = float('-inf')
            if j + 1 < len(B):
                Bright = B[j + 1]
            else:
                Bright = float('inf')
                
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright, Bright)
                return ((max(Aleft, Bleft) + min(Aright, Bright)) / 2.0)
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1