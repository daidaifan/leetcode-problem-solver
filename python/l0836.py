class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        def isOverlap(x1, x2, x3, x4):
            if x1 == x3 and x2 == x4:
                return True
            elif x1 < x3 < x2 or x1 < x4 < x2 or x3 < x1 < x4 or x3 < x2 < x4:
                return True
            return False

        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if isOverlap(x1, x2, x3, x4) and isOverlap(y1, y2, y3, y4):
            return True
        return False


s = Solution()
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
r = s.isRectangleOverlap(rec1, rec2)
print(r)
rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
r = s.isRectangleOverlap(rec1, rec2)
print(r)
