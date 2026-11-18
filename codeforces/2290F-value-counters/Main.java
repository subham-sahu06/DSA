import java.io.*;
public class Main {
    static DataInputStream in = new DataInputStream(new BufferedInputStream(System.in, 1 << 16));
    static int next() throws IOException {
        int r = 0, b = in.read();
        while (b != '-' && (b < '0' || b > '9')) b = in.read();
        boolean neg = false;
        if (b == '-') {
            neg = true;
            b = in.read();
        }
        while (b >= '0' && b <= '9') {
            r = r * 10 + b - '0';
            b = in.read();
        }
        return neg ? -r : r;
    }
    public static void main(String[] args) throws IOException {
        int t = next();
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = next();
            int[] p = new int[n];
            boolean ok = true;
            for (int v = 1; v <= n; v++) {
                int i = next() + n - v;
                if (!ok) continue;
                if (i < 0 || i >= n || p[i] != 0) ok = false;
                else p[i] = v;
            }
            if (!ok) {
                sb.append("-1\n");
                continue;
            }
            for (int i = 0; i < n; i++) sb.append(p[i]).append(i + 1 < n ? ' ' : '\n');
        }
        System.out.print(sb);
    }
}
