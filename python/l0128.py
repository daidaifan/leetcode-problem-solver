class Solution(object):
    def longestConsecutive(self, nums):
        hash_lcs = {}
        for num in nums:
            hash_lcs[num] = 1
        max_lcs = 0
        current_lcs = 0
        last_num = None
        # O(len(nums)) = O(n)
        for num in sorted(hash_lcs.keys()):
            if last_num is not None and last_num + 1 == num:
                current_lcs += 1
                if max_lcs < current_lcs:
                    max_lcs = current_lcs
            else:
                current_lcs = 1

            last_num = num

        return max_lcs



a = [10000, 11, 4, 222, 2, 3, 1]
s = Solution()
print(a)
print(s.longestConsecutive(a))
