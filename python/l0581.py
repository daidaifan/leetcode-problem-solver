"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

    - Time Complexity:
        sorting O(nlog(n)) -> x
        head-tail scan O(n) -> O(n)


    - Space Complexity:
        sorting O(n) -> O(1)

"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import deque
        def merge(left, right):
            result, left, right = deque(), deque(left), deque(right)
            while left and right:
                if left[0] <= right[0]:
                    result.append(left.popleft())
                else:
                    result.append(right.popleft())
            while left or right:
                result.append(left.popleft() if len(left) != 0 else right.popleft())
            return list(result)
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left, right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
            return merge(left, right)
        sorted_nums = merge_sort(nums)

        head, tail = 0, len(nums) - 1
        while nums[head] == sorted_nums[head] or nums[tail] == sorted_nums[tail]:
            if nums[head] == sorted_nums[head]:
                head += 1
            if nums[tail] == sorted_nums[tail]:
                tail -= 1
            if head >= tail:
                return 0
        return tail - head + 1

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        start, end = -1, -2
        min_val, max_val = nums[-1], nums[0]
        for i in range(len(nums)):
            min_val, max_val = min(min_val, nums[len(nums)-1-i]), max(max_val, nums[i])
            if min_val < nums[-1-i]:
                start = len(nums)-1-i
            if max_val > nums[i]:
                end = i
        return end - start + 1

s = Solution()
nums = [4, 542, 66, 12, 4345, 90, 4343, 5567]
print(nums)
print(s.findUnsortedSubarray(nums))


"""
Java O(n) Time O(1) Space
I use the variables beg and end to keep track of minimum subarray A[beg...end]
which must be sorted for the entire array A to be sorted. If end < beg < 0
at the end of the for loop, then the array is already fully sorted.

public int findUnsortedSubarray(int[] A) {
    int n = A.length, beg = -1, end = -2, min = A[n-1], max = A[0];
    for (int i=1;i<n;i++) {
      max = Math.max(max, A[i]);
      min = Math.min(min, A[n-1-i]);
      if (A[i] < max) end = i;
      if (A[n-1-i] > min) beg = n-1-i;
    }
    return end - beg + 1;
}
"""
