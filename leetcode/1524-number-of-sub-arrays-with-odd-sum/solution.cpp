class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const long long MOD = 1000000007;
        long long odd = 0, even = 1, ans = 0;
        int sum = 0;
        for (int x : arr) {
            sum += x;
            if (sum % 2 == 1) {
                ans += even;
                odd++;
            } else {
                ans += odd;
                even++;
            }
        }
        return ans % MOD;
    }
};
