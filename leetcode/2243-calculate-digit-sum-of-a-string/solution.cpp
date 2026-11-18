class Solution {
public:
    string digitSum(string s, int k) {
        while ((int)s.size() > k) {
            string next;
            for (int i = 0; i < (int)s.size(); i += k) {
                int sum = 0;
                int end = min(i + k, (int)s.size());
                for (int j = i; j < end; j++) sum += s[j] - '0';
                next += to_string(sum);
            }
            s = next;
        }
        return s;
    }
};
