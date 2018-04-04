class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num_candidates = 0
        for index, val in enumerate(flowerbed):
            if (index == 0 and val == 0 and len(flowerbed) > 1 and flowerbed[index+1] == 0):
                num_candidates += 1
                flowerbed[index] = 1
            elif(index == len(flowerbed)-1 and val == 0 and flowerbed[index-1] == 0):
                num_candidates += 1
                flowerbed[index] = 1
            elif val == 0 and flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
                num_candidates += 1
                flowerbed[index] = 1
        return n <= num_candidates
