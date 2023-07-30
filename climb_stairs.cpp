class Solution {
public:
    int climbStairs(int n) {
        long memoized[n+1];
        memoized[0] = 0;
        memoized[1] = 1;
        if (n > 1) {
            memoized[2] = 2;
        }
        for (int i=3; i < n+1; i++) {
            memoized[i] = memoized[i-2] + memoized[i-1];
            // cout << "i=" << i << ": " << memoized[i] << '\n';
        };
        return memoized[n];
    }
};