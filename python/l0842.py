class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def helper(S, ans, index):
            if index == len(S) and len(ans) >= 3:
                return ans
            for i in range(index, len(S)):
                num = int(S[index:i+1])
                if S[index] == '0' and i > index:
                    break
                if len(ans) >= 2 and num > ans[-1] + ans[-2]:
                    break
                if num < ans[-1] or num < ans[-2]:
                    break
                if len(ans) < 2 or num == ans[-1] + ans[-2]:
                    ans.append(num)
                    if helper(S, ans, i+1):
                        return ans
                    del ans[-1]
            return []
        return helper(S, [], 0)

s = Solution()
r = s.splitIntoFibonacci('112358139')
print(r)
r = s.splitIntoFibonacci('11235813')
print(r)

"""
public List<Integer> splitIntoFibonacci(String S) {
    List<Integer> ans = new ArrayList<>();
    helper(S, ans, 0);
    return ans;
}

public boolean helper(String s, List<Integer> ans, int idx) {
    if (idx == s.length() && ans.size() >= 3) {
        return true;
    }
    for (int i=idx; i<s.length(); i++) {
        if (s.charAt(idx) == '0' && i > idx) {
            break;
        }
        long num = Long.parseLong(s.substring(idx, i+1));
        if (num > Integer.MAX_VALUE) {
            break;
        }
        int size = ans.size();
        // early termination
        if (size >= 2 && num > ans.get(size-1)+ans.get(size-2)) {
            break;
        }
        if (size <= 1 || num == ans.get(size-1)+ans.get(size-2)) {
            ans.add((int)num);
            // branch pruning. if one branch has found fib seq, return true to upper call
            if (helper(s, ans, i+1)) {
                return true;
            }
            ans.remove(ans.size()-1);
        }
    }
    return false;
}
"""
