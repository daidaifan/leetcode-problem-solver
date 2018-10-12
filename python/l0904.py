"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length


If I start from a tree I can't stop and have to put the fruit in a basket, but I want basket to have only one type of fruit. It is not clear if one needs to stop after a 3rd type of fruit is encountered.

Since about 4 contests there is at least one question that is harder to understand than to solve. Is it too hard to have someone proofread it before posting?
"""

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        type2freq = {}
        set_type = set()
        head = tail = 0
        max_collect = 0
        while tail < len(tree):
            t = tree[tail]
            if t not in set_type:
                set_type.add(t)
            type2freq[t] = type2freq.get(t, 0) + 1
            while len(set_type) > 2:
                remove_t = tree[head]
                type2freq[remove_t] -= 1
                if type2freq[remove_t] == 0:
                    set_type.remove(remove_t)
                head += 1
            max_collect = max(max_collect, tail - head + 1)
            tail += 1
        return max_collect


s = Solution()
print(s.totalFruit([1,2,1]))
print(s.totalFruit([0,1,2,2]))
print(s.totalFruit([1,2,3,2,2]))
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
