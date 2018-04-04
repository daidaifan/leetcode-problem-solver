# 1 two sum
class Solution(object):
    def twoSum(self, nums, target):
        num2index = {}
        # time complexity: O(n), space complexity: O(n)
        for index, num in enumerate(nums):
            # target = num + another_num
            # another_num = target - num
            another_num = target - num
            if another_num in num2index:
                return [index, num2index[another_num]]
            num2index[num] = index

class Solution(object):
    def twoSum(self, nums, target):
        nums = [(num, index) for index, num in enumerate(nums)]
        nums = sorted(nums, key=lambda x: (x[0], x[1]))
        low, high = 0, len(nums) - 1
        while low < high:
            if nums[low][0] + nums[high][0] == target:
                return [nums[low][1], nums[high][1]]
            elif nums[low][0] + nums[high][0] > target:
                high -= 1
            else:
                low += 1

# 15 three sum
class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)

        solution = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
			# a + b + c = target
			# b + c = target - a
            target = -nums[i]
            low, high = i + 1, len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == target:
                    solution.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    low += 1
        return solution

# 18 four sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        solution = []
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                low, high = j + 1, len(nums) - 1
                # a + b + c + d = target
                # c + d = target - a - b
                sub_target = target - nums[i] - nums[j]
                while low < high:
                    if nums[low] + nums[high] == sub_target:
                        solution.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] > sub_target:
                        high -= 1
                    else:
                        low += 1
        return solution

# 454 four sum 2 - four list
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        ab2sum = {}
        for a in A:
            for b in B:
                val = a + b
                ab2sum[val] = ab2sum.get(val, 0) + 1
        solution = 0
        for c in C:
            for d in D:
                val = c + d
                solution += ab2sum.get(-val, 0)
        return solution

# 167 2 sum 2 - input is sorted

class Solution(object):
    def twoSum(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low += 1

# 560 subarray sum equals k
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        accu2sum = {0: 1}
        accu = 0
        solution = 0
        for num in nums:
            accu += num
            # accu - accu_old = k
            accu_old = accu - k
            solution += accu2sum.get(accu_old, 0)
            accu2sum[accu] = accu2sum.get(accu, 0) + 1
        return solution

# 523 continuous subarray sum
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        accu2index = {0: -1}
        accu = 0
        for index, num in enumerate(nums):
            accu += num
            if k != 0:
                accu %= k
            if accu in accu2index and index - accu2index[accu] > 1:
                return True
            accu2index[accu] = accu2index.get(accu, index)
        return False
# 653 two sum 4 - input is bst
class Solution(object):
    def findTarget(self, root, k):
        def travel(node, values, k):
            if node is None:
                return False
            if node.val in values:
                return True
            values.add(k-node.val)
            return travel(node.left, values, k) or travel(node.right, values, k)

        return travel(root, set(), k)
# 78 subset

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start_index, nums, sub_solution, solution):
            if start_index == len(nums):
                solution.append(list(sub_solution))
                return
            dfs(start_index + 1, nums, sub_solution, solution)
            sub_solution.append(nums[start_index])
            dfs(start_index + 1, nums, sub_solution, solution)
            sub_solution.pop()
        solution = []
        dfs(0, nums, [], solution)
        return solution
# 90 subset 2

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def add_sub_solution_to_exist(sub_solution, exist, solution):
            key = tuple(sub_solution)
            if key not in exist:
                solution.append(key)
                exist.add(key)

        def travel(start_index, nums, exist, sub_solution, solution):
            if start_index == len(nums):
                return
            # not choose
            add_sub_solution_to_exist(sub_solution, exist, solution)
            travel(start_index + 1, nums, exist, sub_solution, solution)
            # choose
            sub_solution.append(nums[start_index])
            add_sub_solution_to_exist(sub_solution, exist, solution)
            travel(start_index + 1, nums, exist, sub_solution, solution)
            sub_solution.pop()

        nums = sorted(nums)
        solution = []
        travel(0, nums, set(), [], solution)
        return solution

# 13 roman to integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0
        while i < len(s):
            n1 = mapping[s[i]]
            n2 = mapping[s[i+1]] if i+1 <= len(s) - 1 else 0
            if n2 > n1:
                total += n2 - n1
                i += 1
            else:
                total += n1
            i += 1
        return total

# 20 valid parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            else:
                if len(stack) == 0 or s[i] != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0

# 258 add digits
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            new_num = 0
            while num != 0:
                new_num += num % 10
                num /= 10
            num = new_num
        return num

# 202 happy number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n /= 10
            n = new_n
        return True

# 263 ugly number
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for factor in (2, 3, 5):
            while num % factor == 0 and num > 0:
                num /= factor
        return num == 1

# 264 ugly number 2
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2, i3, i5 = 0, 0, 0
        solution = [1]
        for i in range(1, n):
            ugly = min(2 * solution[i2], 3 * solution[i3], 5 * solution[i5])
            solution.append(ugly)
            if ugly == 2 * solution[i2]:
                i2 += 1
            if ugly == 3 * solution[i3]:
                i3 += 1
            if ugly == 5 * solution[i5]:
                i5 += 1
        return solution[n-1]

# 313 super ugly number
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        def get_min_next_val(solution, parameters, primes):
            min_val = solution[parameters[0]] * primes[0]
            for i in range(1, len(parameters)):
                min_val = min(min_val, solution[parameters[i]] * primes[i])
            return min_val

        solution = [1]
        parameters = [0] * len(primes)
        for i in range(1, n):
            min_next_val = get_min_next_val(solution, parameters, primes)
            solution.append(min_next_val)
            for j in range(len(parameters)):
                if min_next_val == solution[parameters[j]] * primes[j]:
                    parameters[j] += 1
        return solution[n-1]

# 204 count primes
# less than n
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [True] * (n)
        solution = 0
        for i in range(2, n):
            if dp[i] == True:
                dp[i] = False
                solution += 1
                j = 2
                while i * j < n:
                    dp[i * j] = False
                    j += 1
        return solution

# 279 perfect squares
# remember to 'j += 1'
# note initial value of solution[0]
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        solution = [n + 1] * (n + 1)
        solution[0] = 0
        for i in range(1, n + 1):
            j = 1
            while i - j * j >= 0:
                solution[i] = min(solution[i], solution[i - j * j] + 1)
                j += 1
        return solution[n]

# 593 valid square
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def compute_dis(pa, pb):
            return (pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2
        ps = [p1, p2, p3, p4]
        dis2count = {}
        for i in range(len(ps)):
            for j in range(i+1, len(ps)):
                dis = compute_dis(ps[i], ps[j])
                dis2count[dis] = dis2count.get(dis, 0) + 1
        return len(dis2count.keys()) == 2 and (dis2count.values() in ([2, 4], [4, 2]))

# 17 letter combinations of a phone number
# in loop-start_index, only address the digit in index start_index
class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        def dfs(start_index, digits, mapping, sub_solution, solution):
			# terminal condition
            if start_index == len(digits):
                solution.append(''.join(sub_solution))
                return
            # state transition
            digit = int(digits[start_index])
            for j in range(0, len(mapping[digit])):
                sub_solution.append(mapping[digit][j])
                dfs(start_index + 1, digits, mapping, sub_solution, solution)
                sub_solution.pop()
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        solution = []
        dfs(0, digits, mapping, [], solution)
        return solution

# 22 generate parentheses
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(n, n_left, sub_solution, solution):
            # ternimal condition
            if n == 0 and n_left == 0:
                solution.append(''.join(sub_solution))
                return
            # state transition
            if n > 0:
                sub_solution.append('(')
                dfs(n - 1, n_left + 1, sub_solution, solution)
                sub_solution.pop()
            if n_left > 0:
                sub_solution.append(')')
                dfs(n, n_left - 1, sub_solution, solution)
                sub_solution.pop()
        solution = []
        dfs(n, 0, [], solution)
        return solution

# 39 combination sum
# all combination to compose k, can be duplicated
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start_index, candidates, remain, sub_solution, solution):
            # terminal condition
            if remain == 0:
                solution.append(list(sub_solution))
                return
            # state transition
            for i in range(start_index, len(candidates)):
                if candidates[i] <= remain:
                    sub_solution.append(candidates[i])
                    dfs(i, candidates, remain - candidates[i], sub_solution, solution)
                    sub_solution.pop()
        solution = []
        dfs(0, candidates, target, [], solution)
        return solution



# 217 combination sum 3
# 1-9, all combination to compose k with only use n numbers
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(start_num, k, n, sub_solution, solution):
            # terminal condition
            if k == 0 and n == 0:
                solution.append(list(sub_solution))
                return
            # state transition
            for num in range(start_num, 10):
                if k >= 0 and n - num >= 0:
                    sub_solution.append(num)
                    dfs(num + 1, k - 1, n - num, sub_solution, solution)
                    sub_solution.pop()
        solution = []
        dfs(1, k, n, [], solution)
        return solution
# 377 combination sum 4
# how many combination to reach target
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]
        return dp[target]

# 77 combination
# c n choose k combination
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        def dfs(start_num, n, k, sub_solution, solution):
            # terminal condition
            if k == 0:
                solution.append(list(sub_solution))
                return
            if start_num > n:
                return
            # state transition
            dfs(start_num + 1, n, k, sub_solution, solution)
            sub_solution.append(start_num)
            dfs(start_num + 1, n, k - 1, sub_solution, solution)
            sub_solution.pop()
        solution = []
        dfs(1, n, k, [], solution)
        return solution

# 228 summary ranges
# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# note that the comparison containing nums[tail + 1], so condition is tail < len(nums) - 1
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        head, tail = 0, 0
        solution = []
        while head < len(nums):
            while tail < len(nums) - 1 and nums[tail] + 1 == nums[tail + 1]:
                tail += 1
            if head != tail:
                solution.append('{}->{}'.format(nums[head], nums[tail]))
            else:
                solution.append('{}'.format(nums[tail]))
            head = tail = tail + 1
        return solution

# 33 search in rotated sorted array
# binary search: very hard
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
			# 3 4 5   6   7 1 2
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
			# 6 7 1   2   3 4 5
            elif nums[low] > nums[mid]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
# 81 search in rotated sorted array 2
# binary search: very hard
# modify two points: (1) nums[low] <= nums[mid] -> nums[low] < nums[mid] (2) else: low += 1
# 3 1 2   3   3 3 3
# 3 3 3   3   1 2 3
# worst case O(n) because input may [2, 2, 2, 2, 2, 2, 2] search 1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            elif nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1
        return False

# 670 maximum swap
# remember the mappint from 1-9 to their last happen index
# note check from 9 to (d + 1) -> range(9, d, -1)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        s = map(int, s)
        d2i = {}
        for index, d in enumerate(s):
            d2i[d] = index
        for index, d in enumerate(s):
            for i in range(9, d, -1):
                if i in d2i and d2i[i] > index:
                    s[index], s[d2i[i]] = s[d2i[i]], s[index]
                    return int(''.join(map(str, s)))
        return num

# 28 implement strStr()
class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1


# 38 count and say
class Solution(object):
    def countAndSay(self, n):
        last_str = '1'
        for i in range(1, n):
            chars = [last_str[0]]
            sizes = [1]
            for j in range(1, len(last_str)):
                if chars[-1] == last_str[j]:
                    sizes[-1] += 1
                else:
                    chars.append(last_str[j])
                    sizes.append(1)
            last_str = ''.join([str(size) + char for size, char in zip(sizes, chars)])
        return last_str

# quick selection
def quickselect(items, item_index):

    def select(lst, l, r, index):

        # base case
        if r == l:
            return lst[l]

        # choose random pivot
        pivot_index = random.randint(l, r)

        # move pivot to beginning of list
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # partition
        i = l
        for j in xrange(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # move pivot to correct location
        lst[i], lst[l] = lst[l], lst[i]

        # recursively partition one side only
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i-1, index)
        else:
            return select(lst, i+1, r, index)

    if items is None or len(items) < 1:
        return None

    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()

    return select(items, 0, len(items) - 1, item_index)

# 215 kth largest element in an array
# smallest: 'nums[j] > nums[l]' -> '<', 'k - 1' -> 'len(nums) - k'
# average case: O(n), worst case O(n^2)
class Solution(object):
    import random
    def findKthLargest(self, nums, k):
        def qselect(nums, l, r, k):
            if l == r:
                return nums[l]
            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[l] = nums[l], nums[pivot_index]
            i = l
            for j in range(l + 1, r + 1):
                if nums[j] > nums[l]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            if k == i:
                return nums[i]
            elif k < i:
                return qselect(nums, l, i - 1, k)
            else:
                return qselect(nums, i + 1, r, k)
        return qselect(nums, 0, len(nums) - 1, k - 1)
# 206 reverse linked list
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous_node = None
        next_node = None
        while head:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node
        return previous_node
# 283 move zeroes
class Solution(object):
    def moveZeroes(self, nums):
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
# 27 remove element (remove target)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        non_target_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[non_target_index] = nums[i]
                non_target_index += 1
        for i in range(non_target_index, len(nums)):
            nums.pop()
        return len(nums)
# 278 first bad version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# CAN NOT add equal in 'low < high' statement
# edge case: input 1
class Solution(object):
    def firstBadVersion(self, n):
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid) == True:
                high = mid
            else:
                low = mid + 1
        return high
# 436 find right interval
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        pairs = [(interval.start, index) for index, interval in enumerate(intervals)]
        pairs = sorted(pairs, key=lambda x: (x[0]))
        solution = []
        for interval in intervals:
            low, high = 0, len(pairs) - 1
            end = interval.end
            while low < high:
                mid = low + (high - low) // 2
                if pairs[mid][0] < end:
                    low = mid + 1
                else:
                    high = mid
            s = pairs[high][1] if end <= pairs[high][0] else -1
            solution.append(s)
        return solution

class Solution(object):
    def findRightInterval(self, intervals):
        start2index = {}
        starts = []
        for i in range(len(intervals)):
            start = intervals[i].start
            start2index[start] = i
            starts.append(start)
        starts = sorted(starts)
        solution = []
        for interval in intervals:
            low, high = 0, len(starts) - 1
            end = interval.end
            while low < high:
                mid = low + (high - low) // 2
                if starts[mid] < end:
                    low = mid + 1
                else:
                    high = mid
            s = start2index[starts[high]] if end <= starts[high] else -1
            solution.append(s)
        return solution

# 461 hamming distance
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        while x != 0 or y != 0:
            if (x & 1) != (y & 1):
                distance += 1
            x >>= 1
            y >>= 1
        return distance
# 397 integer replacement
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(n):
            if n == 1:
                return 0
            elif (n & 1) == 0:
                return dfs(n//2) + 1
            else:
                return min(dfs(n+1) + 1, dfs(n-1) + 1)
        return dfs(n)

# fb-interview tasks
class Solution(object):
    def compute_time(self, tasks, cooldown):
        task2time = {}
        total_time = 0
        for this_task in tasks:
            if this_task not in task2time or total_time - task2time[this_task] > cooldown:
                task2time[this_task] = total_time
                total_time += 1
            else:
                total_time = task2time[this_task] + (cooldown + 1)
                task2time[this_task] = total_time
                total_time += 1
        return total_time

# 621 task schedule
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task2freq = {}
        max_size = 0
        for task in tasks:
            task2freq[task] = task2freq.get(task, 0) + 1
            if max_size < task2freq[task]:
                max_size = task2freq[task]
        num_max_size_task = sum([1 for task, freq in task2freq.items() if freq == max_size])
        return max(len(tasks), (max_size - 1) * (n + 1) + num_max_size_task)

# bruteforce subset sum
from itertools import combinations
def subsetsum(numbers, target):
   size = 1
   subsets = []
   while size <= len(numbers):
      for combination in combinations(numbers, size):
         if sum(combination) == target:
            subsets.append(combination)
      size += 1
   return subsets

def combinations(numbers, size):
   if len(numbers) <= 0 or size <= 0:
      return []
   else:
      for index, number in enumerate(numbers):
         for combination in combinations(numbers[index+1:], size-1):
            return [number] + combination

# 235 lowest common ancestor of a binary search tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return root
        elif min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        elif root.val <= min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val >= max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
# 236 lowest common ancestor of a binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left_node = self.lowestCommonAncestor(root.left, p, q)
        right_node = self.lowestCommonAncestor(root.right, p, q)
        if left_node is not None and right_node is not None:
            return root
        return left_node or right_node

# 69 sqrt
# note that no equal sign in condition 'mid ** 2 <= x < (mid + 1) ** 2
class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        low, high = 1, x
        while low < high:
            mid = low + (high - low) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                break
            elif mid ** 2 > x:
                high = mid
            else:
                low = mid
        return mid

# 367 valid perfect square
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        while low <= high:
            mid = low + (high - low) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1
        return False

# 50 pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        # 2 ^ -3 -> (1/2) ^ 3
        if n < 0:
            n = -n
            x = 1 / x
        solution = 1
        while n > 0:
            if (n & 1) == 1:
                solution *= x
            x *= x
            n >>= 1
        return solution

# 372 super pow
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b = int(''.join(map(str, b)))
        solution = 1
        while b > 0:
            if (b & 1) == 1:
                solution *= a
            a *= a
            b >>= 1
            a %= 1337
            solution %= 1337
        return solution
# 633 sum of square numbers
# two pointers
# note that left starts from '0'
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(c ** 0.5)
        while left <= right:
            val = left ** 2 + right ** 2
            if val == c:
                return True
            elif val > c:
                right -= 1
            else:
                left += 1
        return False

# 138 word break
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] is True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        solution = [False] * (len(s) + 1)
        solution[0] = True
        for i in range(1, len(s) + 1):
            for j in range(1, i + 1):
                if solution[i-j] is True and s[i-j:i] in wordDict:
                    solution[i] = True
                    break
        return solution[len(s)]
<<<<<<< HEAD

# 139 word break
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i] == False:
                continue
            for w in wordDict:
                if i + len(w) > len(s):
                    continue
                pattern = s[i:i+len(w)]
                if pattern == w:
                    dp[i+len(w)] = True
        return dp[len(s)]
# 140 word break 2
# Original memorized dfs
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def dfs(s, wordDict, s2composition):
            if s in s2composition:
                return s2composition[s]
            if len(s) == 0:
                return ['']
            composition = []
            for w in wordDict:
                if w == s[:len(w)]:
                    sub_composition = dfs(s[len(w):], wordDict, s2composition)
                    for sub in sub_composition:
                        if sub == '':
                            composition.append(w)
                        else:
                            composition.append(w + ' ' + sub)
            s2composition[s] = composition
            return composition

        return dfs(s, wordDict, {})

# simple dfs
# will TLE if input is aaaaaaaaaaaaaaaaaaaaaaaaa, ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', ...]
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def dfs(start_index, s, wordDict, sub_solution, solution):
            # terminal condition
            if start_index == len(s):
                solution.append(' '.join(sub_solution))
                return
            # state transition
            for w in wordDict:
                if start_index + len(w) > len(s):
                    continue
                if w == s[start_index:start_index + len(w)]:
                    sub_solution.append(w)
                    dfs(start_index + len(w), s, wordDict, sub_solution, solution)
                    sub_solution.pop()
        solution = []
        dfs(0, s, wordDict, [], solution)
        return solution

# improved memorized dfs
# time complexity = O( len(wordDict) ^ len(s / min_word_length) ) -> O( len(wordDict) * len(s / min_word_length) )
class Solution(object):
    def wordBreak(self, s, wordDict):
        def dfs(s, wordDict, s2composition):
            # memorized look up
            if s in s2composition:
                return s2composition[s]
            # terminal condition
            if len(s) == 0:
                return [[]]
            # state transition
            composition = []
            for w in wordDict:
                if w == s[:len(w)]:
                    sub_composition = dfs(s[len(w):], wordDict, s2composition)
                    for sub in sub_composition:
                        composition.append([w] + sub)
            s2composition[s] = composition
            return composition

        composition = dfs(s, wordDict, {})
        return [' '.join(c) for c in composition]

# 472 concatenated words
# very hard
# dfs will be TLE
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        def canCompose(s, words):
            # input: ['']
            if len(words) == 0:
                return False
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(1, len(s) + 1):
                for j in range(i):
                    if dp[j] == True and s[j:i] in words:
                        dp[i] = True
                        break
            return dp[len(s)]
        solution = []
        available_words = set()
        words = sorted(words, key=lambda x: len(x))
        for word in words:
            if canCompose(word, available_words):
                solution.append(word)
            available_words.add(word)
        return solution
# 56 merge intervals
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: (x.start, -x.end))
        solution = []
        start, end = None, None
        for interval in intervals:
            if start is None or end is None:
                start, end = interval.start, interval.end
                continue
            elif end >= interval.start:
                end = max(end, interval.end)
            else:
                solution.append(Interval(start, end))
                start, end = interval.start, interval.end
        if start is not None or end is not None:
            solution.append(Interval(start, end))
        return solution

# 79 word search
class Solution(object):
    def exist(self, board, word):
        def dfs(board, i, j, word, start_index):
            # terminal conditions
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False
            if board[i][j] == '*' or board[i][j] != word[start_index]:
                return False
            if start_index == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = '*'
            # state transition
            if dfs(board, i+1, j, word, start_index+1) or dfs(board, i-1, j, word, start_index+1) or dfs(board, i, j+1, word, start_index+1) or dfs(board, i, j-1, word, start_index+1):
                return True
            else:
                board[i][j] = tmp
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(board, i, j, word, 0):
                    return True
        return False
# 88 merge sorted array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        total_index = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 or n >= 0:
            if m >= 0 and n >= 0:
                if nums1[m] >= nums2[n]:
                    nums1[total_index] = nums1[m]
                    m -= 1
                else:
                    nums1[total_index] = nums2[n]
                    n -= 1
            elif n >= 0:
                nums1[total_index] = nums2[n]
                n -= 1
            else:
                break
            total_index -= 1
        return

# 121 best time to buy and sell stock
# transaction only 1 time
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        last_sell = 0
        last_buy = None
        for p in prices:
            if last_buy is None:
                last_buy = p
                continue
            last_sell = max(last_sell, p - last_buy)
            last_buy = min(last_buy, p)
        return last_sell
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        sell = 0
        buy = -sys.maxint - 1
        for p in prices:
            sell = max(sell, buy + p)
            buy = max(buy, -p)
        return sell

# 122 best time to buy and sell stock 2
# transaction infinite times
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
        return profit

# 123 best time to buy and sell stock 3
# transaction 2 times
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        import sys
        second_sell = 0
        second_buy = -sys.maxint - 1
        first_sell = 0
        first_buy = -sys.maxint - 1
        for p in prices:
            second_sell = max(second_sell, second_buy + p)
            second_buy = max(second_buy, first_sell - p)
            first_sell = max(first_sell, first_buy + p)
            first_buy = max(first_buy, -p)
        return max(second_sell, first_sell)

# 188 best time to buy and sell stock 4
# transaction k times
# TLE version
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        import sys
        sell = [0] * (k + 1)
        buy = [-sys.maxint - 1] * (k + 1)
        for p in prices:
            for i in range(k, 0, -1):
                sell[i] = max(sell[i], buy[i] + p)
                buy[i] = max(buy[i], sell[i-1] - p)
        return max(sell)
# add quick solver to address the situation that k is enough
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def quickSolver(prices):
            profit = 0
            for i in range(len(prices) - 1):
                if prices[i + 1] - prices[i] > 0:
                    profit += prices[i + 1] - prices[i]
            return profit

        if k >= len(prices) // 2:
            return quickSolver(prices)

        import sys
        sell = [0] * (k + 1)
        buy = [-sys.maxint - 1] * (k + 1)
        for p in prices:
            for i in range(k, 0, -1):
                sell[i] = max(sell[i], buy[i] + p)
                buy[i] = max(buy[i], sell[i-1] - p)
        return max(sell)

# 309 best time to buy and sell stock with cooldown
# transaction infinite times
# buy[i] = max(sell[i-2]-price, buy[i-1])
# sell[i] = max(buy[i-1]+price, sell[i-1])
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev_sell, sell = 0, 0
        prev_buy, buy = None, -sys.maxint-1
        for price in prices:
            prev_buy = buy
            buy = max(prev_buy, prev_sell-price)
            prev_sell = sell
            sell = max(prev_sell, prev_buy+price)
        return sell
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        sell = [0] * (len(prices) + 1)
        buy = [-sys.maxint - 1] * (len(prices) + 1)
        for i, p in zip(range(1, len(prices) + 1), prices):
            sell[i] = max(sell[i-1], buy[i-1] + p)
            if i - 2 >= 0:
                buy[i] = max(buy[i-1], sell[i-2] - p)
            else:
                buy[i] = - p
        return sell[len(prices)]

# 714 best time to buy and sell stock with transaction fee
# transaction infinite times
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        import sys
        sell, buy = 0, -sys.maxint-1
        for p in prices:
            prev_sell = sell
            sell = max(sell, buy+p)
            buy = max(buy, prev_sell - p - fee)
        return sell

# 53 max subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        global_max = nums[0]
        local_max = nums[0]
        for i in range(1, len(nums)):
            if local_max < 0:
                local_max = 0
            local_max += nums[i]
            if global_max < local_max:
                global_max = local_max
        return global_max

# 91 decode ways
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        for i in range(len(s)):
            if i == 0 and 1 <= int(s[i]) <= 9:
                dp[0] = dp[1] = 1
                continue
            elif 1 <= int(s[i]) <= 9:
                dp[i+1] = dp[i]
            if i >= 1 and 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[len(s)]

#639 decode ways
def numDecodings(self, S):
    MOD = 10**9 + 7
    e0, e1, e2 = 1, 0, 0
    for c in S:
        if c == '*':
            f0 = 9*e0 + 9*e1 + 6*e2
            f1 = e0
            f2 = e0
        else:
            f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
            f1 = (c == '1') * e0
            f2 = (c == '2') * e0
        e0, e1, e2 = f0 % MOD, f1, f2
    return e0
# e0 = current number of ways we could decode, ending on any number;
# e1 = current number of ways we could decode, ending on an open 1;
# e2 = current number of ways we could decode, ending on an open 2;
class Solution(object):
    def numDecodings(self, s):
        mod = 10 ** 9 + 7
        end_any, end_1, end_2 = 1, 0, 0
        for c in list(s):
            if c == '*':
                t_1 = end_any
                t_2 = end_any
                t_any = 9 * end_any + 9 * end_1 + 6 * end_2
            else:
                t_1 = (c == '1') * end_any
                t_2 = (c == '2') * end_any
                t_any = (c >= '1') * end_any + end_1 + (c <= '6') * end_2
            end_any, end_1, end_2 = t_any % mod, t_1, t_2
        return end_any

# 416 partition equal subset sum
class Solution(object):
    def canPartition(self, nums):
        if len(nums) == 0:
            return True
        if sum(nums) & 1 != 0:
            return False
        def dfs(target, cur_sum, nums):
            if target == cur_sum:
                if len(nums) == 0:
                    return True
                return dfs(target, nums[-1], nums[:-1])
            for i in range(len(nums)):
                tried_val = nums[i]
                if cur_sum + tried_val <= target:
                    nums[-1], nums[i] = nums[i], nums[-1]
                    if dfs(target, tried_val + cur_sum, nums[:-1]):
                        return True
                    nums[i], nums[-1] = nums[-1], nums[i]
            return False

        nums.sort()
        return dfs(sum(nums)//2, nums[-1], nums[:-1])
# 198 house robber
class Solution(object):
    def rob(self, nums):
        result = [0, 0]
        for num in nums:
            result[0], result[1] = max(result[0], result[1]), num + result[0]
        return max(result)

# 213 house robber 2
class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        def do_rob(nums, low, high):
            result = [0, 0]
            for i in range(low, high+1):
                result[0], result[1] = max(result[0], result[1]), nums[i] + result[0]
            return max(result)
        return max(do_rob(nums, 1, len(nums)-1), do_rob(nums, 0, len(nums)-2))
# 337 house robber 3
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def do_rob(node):
            if node is None:
                return [0, 0]
            left_result = do_rob(node.left)
            right_result = do_rob(node.right)
            result = [0, 0]
            result[0] = max(left_result[0], left_result[1]) + max(right_result[0], right_result[1])
            result[1] = node.val + left_result[0] + right_result[0]
            return result
        result = do_rob(root)
        return max(result)

# 207 course schedule
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        src2dst = {}
        for dst, src in prerequisites:
            if src not in src2dst:
                src2dst[src] = []
            src2dst[src].append(dst)
        while len(src2dst) != 0:
            # all constraint course
            visited_dsts = set()
            for dsts in src2dst.values():
                for dst in dsts:
                    visited_dsts.add(dst)
            orig_len = len(src2dst)
            for src in src2dst.keys():
                # no constraint course: src
                if src not in visited_dsts:
                    del src2dst[src]
            if orig_len == len(src2dst):
                return False
        return True
# 208 course schedule 2
# just add the learning sequence
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        src2dsts = {}
        for dst, src in prerequisites:
            if src not in src2dsts:
                src2dsts[src] = []
            src2dsts[src].append(dst)
        sequence = []
        remaining_pool = set()
        for i in range(numCourses):
            remaining_pool.add(i)
        while len(src2dsts) != 0:
            visited_dsts = set()
            for dsts in src2dsts.values():
                for dst in dsts:
                    visited_dsts.add(dst)
            original_len = len(src2dsts)
            for src in src2dsts.keys():
                if src not in visited_dsts:
                    sequence.append(src)
                    del src2dsts[src]
                    if src in remaining_pool:
                        remaining_pool.remove(src)
            if original_len == len(src2dsts):
                return []
        for dst in remaining_pool:
            sequence.append(dst)
        return sequence
# 630 course schedule 3
# priority queue
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        import heapq
        courses = sorted(courses, key=lambda x: (x[1], x[0]))
        start = 0
        pq = []
        for time, due in courses:
            heapq.heappush(pq, -time)
            start += time
            while start > due:
                start += heapq.heappop(pq)
        return len(pq)

>>>>>>> e94e2e1e55b96468f0f4b036049d9ac859be7862
