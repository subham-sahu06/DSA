import java.io.*;
public class Main {
    static DataInputStream in = new DataInputStream(new BufferedInputStream(System.in, 1 << 16));
    static int next() throws IOException {
        int r = 0, b = in.read();
        while (b < '0') b = in.read();
        while (b >= '0') {
            r = r * 10 + b - '0';
            b = in.read();
        }
        return r;
    }
    public static void main(String[] args) throws IOException {
        int t = next();
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = next(), k = next();
            int[] pre = new int[n + 1];
            int total = 0;
            for (int i = 1; i <= n; i++) {
                int lo = Math.max(1, i - k);
                int x = pre[i - 1] ^ pre[lo - 1];
                int g = x == 0 ? 1 : 0;
                pre[i] = pre[i - 1] ^ g;
                if ((next() & 1) == 1) total ^= g;
            }
            sb.append(total != 0 ? "Alice" : "Bob").append('\n');
        }
        System.out.print(sb);
    }
}
