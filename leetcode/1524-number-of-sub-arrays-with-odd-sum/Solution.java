class Solution {
    public int numOfSubarrays(int[] arr) {
        final int MOD = 1_000_000_007;
        long odd = 0, even = 1, ans = 0;
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
        return (int) (ans % MOD);
    }
}
