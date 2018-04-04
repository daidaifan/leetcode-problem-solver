"""
def countSmaller(nums):
	def sort(enum):
		half = len(enum) / 2
		if half:
			left, right = sort(enum[:half]), sort(enum[half:])
			print('left', left, 'right', right)
			for i in range(len(enum))[::-1]:
				if not right or left and left[-1][1] > right[-1][1]:
					smaller[left[-1][0]] += len(right)
					enum[i] = left.pop()
				else:
					enum[i] = right.pop()
			print('enum', enum)
		return enum
	smaller = [0] * len(nums)
	sort(list(enumerate(nums)))
	return smaller
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(enums):
            if len(enums) <= 1:
                return enums
            mid = len(enums) / 2
            left, right = merge_sort(enums[:mid]), merge_sort(enums[mid:])
            for i in range(len(enums)-1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]:
                    self.solution[left[-1][0]] += len(right)
                    enums[i] = left.pop()
                else:
                    enums[i] = right.pop()
            return enums
        
        
        self.solution = [0] * len(nums)
        nums = merge_sort(list(enumerate(nums)))
        return self.solution
nums = [3, 2, 2, 6, 1, 9, 8, 5, 10]
s = Solution()
print(nums)
print(s.countSmaller(nums))
