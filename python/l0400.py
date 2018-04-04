"""
- 400. Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

    - Key Point:

    - Time Complexity:

    - Space Complexity:

"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        count = 9
        start = 1
        while n > length * count:
            print('n', n, 'length', length, 'count', count, 'length*count', length*count, 'start', start)
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        print('n', n)
        print('start', start)
        start += (n - 1) // length
        print('start', start)
        s = str(start)
        print((n - 1) % length)
        return s[(n - 1) % length]

s = Solution()
print(s.findNthDigit(11))
print(s.findNthDigit(12))
print(s.findNthDigit(13))

print(s.findNthDigit(2 ** 30 + 987))

"""
Straight forward way to solve the problem in 3 steps:

find the length of the number where the nth digit is from
find the actual number where the nth digit is from
find the nth digit and return

    public int findNthDigit(int n) {
        int len = 1;
        long count = 9;
        int start = 1;

        while (n > len * count) {
            n -= len * count;
            len += 1;
            count *= 10;
            start *= 10;
        }

        start += (n - 1) / len;
        String s = Integer.toString(start);
        return Character.getNumericValue(s.charAt((n - 1) % len));
    }
"""
