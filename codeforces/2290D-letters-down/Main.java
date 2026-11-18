import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String s = br.readLine().trim();
            int[] diff = new int[27];
            for (int i = 0; i < n / 2; i++) {
                int u = s.charAt(i) - 'a', v = s.charAt(n - 1 - i) - 'a';
                if (u > v) {
                    int tmp = u;
                    u = v;
                    v = tmp;
                }
                if (u < v) {
                    diff[u + 1]++;
                    diff[v + 1]--;
                }
            }
            int cur = 0, ans = 0;
            for (int c = 0; c < 26; c++) {
                cur += diff[c];
                if (cur > 0) ans++;
            }
            sb.append(ans).append('\n');
        }
        System.out.print(sb);
    }
}
