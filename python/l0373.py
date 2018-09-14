class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        def heap_push(heap, i, j, nums1, nums2):
            if 0 <= i <= len(nums1) - 1 and 0 <= j <= len(nums2) - 1:
                heapq.heappush(heap, [nums1[i] + nums2[j], i, j])

        import heapq
        heap = []
        answer = []
        heap_push(heap, 0, 0, nums1, nums2)
        while len(heap) and len(answer) < k:
            _, i, j = heapq.heappop(heap)
            answer.append((nums1[i], nums2[j]))
            heap_push(heap, i, j+1, nums1, nums2)
            if j == 0:
                heap_push(heap, i+1, 0, nums1, nums2)
        return answer

s = Solution()
r = s.kSmallestPairs([1, 1, 2], [1, 2, 3], 3)
print(r)
