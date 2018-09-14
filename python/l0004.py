class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def GetMedian(a, b, k):
            if len(a) == 0:
                return b[k-1]
            if len(b) == 0:
                return a[k-1]
            if k == 1:
                return min(a[0], b[0])

            max_val = max(a[-1], b[-1]) + 1
            mid_size = k // 2
            mid_index = mid_size - 1
            a_mid = a[mid_index] if mid_index < len(a) else max_val
            b_mid = b[mid_index] if mid_index < len(b) else max_val
            if a_mid < b_mid:
                return GetMedian(a[mid_size:], b, k - mid_size)
            else:
                return GetMedian(a, b[mid_size:], k - mid_size)

        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        if (m + n) % 2 == 1:
            return GetMedian(nums1, nums2, mid + 1)
        return (GetMedian(nums1, nums2, mid + 1) + GetMedian(nums1, nums2, mid)) / 2.0

s = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
r = s.findMedianSortedArrays(nums1, nums2)
print(r)


