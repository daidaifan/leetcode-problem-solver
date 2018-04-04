"""
Cpp solution with explanation in details
It's a very classical question.
Ref: http://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/

class Solution {
public:

    //  Method returns true if nums can be partitioned into K subsets
    // with equal sum
    bool canPartitionKSubsets(vector<int>& nums, int K)
    {
        int N = nums.size();
        //  If K is 1, then complete array will be our answer
        if (K == 1) return true;

        //  If total number of partitions are more than N, then
        // division is not possible
        if (N < K) return false;

        // if array sum is not divisible by K then we can't divide
        // array into K partitions
        int sum = 0;
        for (int i = 0; i < N; i++) sum += nums[i];
        if (sum % K != 0) return false;

        //  the sum of each subset should be subset (= sum / K)
        int subset = sum / K;
        int subsetSum[K];
        bool taken[N];

        //  Initialize sum of each subset from 0
        for (int i = 0; i < K; i++) subsetSum[i] = 0;

        //  mark all elements as not taken
        for (int i = 0; i < N; i++) taken[i] = false;

        // initialize first subsubset sum as last element of
        // array and mark that as taken
        subsetSum[0] = nums[N - 1];
        taken[N - 1] = true;

        //  call recursive method to check K-substitution condition
        return canPartitionKSubsets(nums, subsetSum, taken, subset, K, N, 0, N - 1);
    }

    // Recursive Utility method to check K equal sum
    // subsetition of array
    /**
        array           - given input array
        subsetSum array   - sum to store each subset of the array
        taken           - boolean array to check whether element
                          is taken into sum partition or not
        K               - number of partitions needed
        N               - total number of element in array
        curIdx          - current subsetSum index
        limitIdx        - lastIdx from where array element should be taken
    */
    bool canPartitionKSubsets(vector<int>& nums, int subsetSum[], bool taken[], int subset, int K, int N, int curIdx, int limitIdx) {
        if (subsetSum[curIdx] == subset) {
            /*  current index (K - 2) represents (K - 1) subsets of equal
                sum last partition will already remain with sum 'subset'*/
            if (curIdx == K - 2) return true;

            //  recursive call for next subsetition
            return canPartitionKSubsets(nums, subsetSum, taken, subset,
                                        K, N, curIdx + 1, N - 1);
        }

        //  start from limitIdx and include elements into current partition
        for (int i = limitIdx; i >= 0; i--) {
            //  if already taken, continue
            if (taken[i]) continue;
            int tmp = subsetSum[curIdx] + nums[i];

            // if temp is less than subset then only include the element
            // and call recursively
            if (tmp <= subset) {
                //  mark the element and include into current partition sum
                taken[i] = true;
                subsetSum[curIdx] += nums[i];
                bool nxt = canPartitionKSubsets(nums, subsetSum, taken, subset, K, N, curIdx, i - 1);
                // after recursive call unmark the element and remove from
                // subsetition sum
                taken[i] = false;
                subsetSum[curIdx] -= nums[i];
                if (nxt) return true;
            }
        }
        return false;
    }

};
"""

"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if len(nums) < k or sum(nums) % k != 0 :
            return False
        sub_sum = sum(nums) / k
        if any(num > sub_sum for num in nums):
            return False
        nums.sort()
        return self.dfs(sub_sum,nums[-1], nums[: -1])

    def dfs(self, sub_sum, cur_sum, nums):
        if cur_sum == sub_sum:

            if not nums:
                return True
            return self.dfs(sub_sum, nums[-1], nums[: -1])
        size = len(nums)
        for index in xrange(size):
            tmp = nums[index]
            if nums[index] + cur_sum <= sub_sum:
                nums[index], nums[-1] = nums[-1], nums[index]
                nums.pop()
                if self.dfs(sub_sum, cur_sum + tmp, nums):
                    return True
                nums.append(tmp)
                nums[index], nums[-1] = nums[-1], nums[index]
        return False
"""

"""
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum=0,len=nums.length;
        for(int i:nums) sum+=i;
        if(sum%k!=0) return false;
        int[] sums= new int[k];
        int target=sum/k;
        Arrays.sort(nums);
        return helper(nums,sums,target,len-1);
    }

    public boolean helper(int[]nums,int[] sums,int target,int curidx){
    if(curidx==0){
        for(int i=0;i<sums.length-1;i++){
            if(sums[i]!=target) return false;
        }
        return true;
    }
          for(int i=0;i<sums.length;i++){
              if(sums[i]+nums[curidx]<=target){
                  sums[i]+=nums[curidx];
                  if(helper(nums,sums,target,curidx-1)) return true;
                  sums[i]-=nums[curidx];
              }
          }
        return false;
    }
}
"""



"""
[Java/C++]Straightforward dfs solution
Update: This question has been changed after the contest. It added the special restriction 0 < nums[i] < 10000. My solution here is without that consideration.

Assume sum is the sum of nums[] . The dfs process is to find a subset of nums[] which sum equals to sum/k. We use an array visited[] to record which element in nums[] is used. Each time when we get a cur_sum = sum/k, we will start from position 0 in nums[] to look up the elements that are not used yet and find another cur_sum = sum/k.

An corner case is when sum = 0, my method is to use cur_num to record the number of elements in the current subset. Only if cur_sum = sum/k && cur_num >0, we can start another look up process.

Some test cases may need to be added in:
nums = {-1,1,0,0}, k = 4
nums = {-1,1}, k = 1
nums = {-1,1}, k = 2
nums = {-1,1,0}, k = 2
...

Java version:

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for(int num:nums)sum += num;
        if(k <= 0 || sum%k != 0)return false;
        int[] visited = new int[nums.length];
        return canPartition(nums, visited, 0, k, 0, 0, sum/k);
    }

    public boolean canPartition(int[] nums, int[] visited, int start_index, int k, int cur_sum, int cur_num, int target){
        if(k==1)return true;
        if(cur_sum == target && cur_num>0)return canPartition(nums, visited, 0, k-1, 0, 0, target);
        for(int i = start_index; i<nums.length; i++){
            if(visited[i] == 0){
                visited[i] = 1;
                if(canPartition(nums, visited, i+1, k, cur_sum + nums[i], cur_num++, target))return true;
                visited[i] = 0;
            }
        }
        return false;
    }


C++ version:

    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = 0;
        for(int num:nums)sum+=num;
        if(k <= 0 || sum%k != 0)return false;
        vector<int> visited(nums.size(), 0);
        return canPartition(nums, visited, 0, k, 0, 0, sum/k);
    }

    bool canPartition(vector<int>& nums, vector<int>& visited, int start_index, int k, int cur_sum, int cur_num, int target){
        if(k==1)
            return true;
        if(cur_sum == target && cur_num >0 )
            return canPartition(nums, visited, 0, k-1, 0, 0, target);
        for(int i = start_index; i<nums.size(); i++){
            if(!visited[i]){
                visited[i] = 1;
                if(canPartition(nums, visited, i+1, k, cur_sum + nums[i], cur_num++, target))
                    return true;
                visited[i] = 0;
            }
        }
        return false;
    }
"""



class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if k <= 0 or len(nums) < k or sum(nums) % k != 0:
            return False

        def canPartition(nums, start_index, k, cur_sum, cur_num, target):
            if cur_sum > target:
                return False
            if k == 1:
                return True
            if cur_sum == target and cur_num > 0:
                return canPartition(nums, 0, k-1, 0, 0, target)
            for i in range(start_index, len(nums)):
                if self.visited[i] is False:
                    self.visited[i] = True
                    if canPartition(nums, start_index + 1, k, cur_sum + nums[i], cur_num + 1, target):
                        return True
                    self.visited[i] = False
            return False
        self.visited = [False] * len(nums)
        return canPartition(nums, 0, k, 0, 0, sum(nums) // k)


s = Solution()
print(s.canPartitionKSubsets([4, 5, 3, 2, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5], 14))
print(s.canPartitionKSubsets([780,935,2439,444,513,1603,504,2162,432,110,1856,575,172,367,288,316], 4))

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0 or len(nums) < k or sum(nums) % k != 0:
            return False
        def dfs(target, cur_sum, nums):
            if target == cur_sum:
                if len(nums) == 0:
                    return True
                return dfs(target, nums[-1], nums[:-1])
            for i in range(len(nums)):
                tried_val = nums[i]
                if tried_val + cur_sum <= target:
                    nums[i], nums[-1] = nums[-1], nums[i]
                    if dfs(target, cur_sum + tried_val, nums[:-1]):
                        return True
                    nums[-1], nums[i] = nums[i], nums[-1]
            return False
        nums = sorted(nums)
        return dfs(sum(nums)//k, nums[-1], nums[:-1])
