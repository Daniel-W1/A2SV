class Solution(object):
    def stoneGameIII(self, A):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        dp = [0] * 3
        for i in xrange(len(A) - 1, -1, -1):
            dp[i % 3] = max(sum(A[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        return ["Tie", "Alice", "Bob"][cmp(dp[0], 0)]