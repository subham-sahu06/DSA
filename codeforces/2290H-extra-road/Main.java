import java.io.*;
import java.util.*;
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
            int n = next();
            int[] head = new int[n + 1], nxt = new int[2 * n], to = new int[2 * n];
            Arrays.fill(head, -1);
            for (int i = 0; i < n - 1; i++) {
                int u = next(), v = next();
                to[2 * i] = v; nxt[2 * i] = head[u]; head[u] = 2 * i;
                to[2 * i + 1] = u; nxt[2 * i + 1] = head[v]; head[v] = 2 * i + 1;
            }
            int[] par = new int[n + 1], order = new int[n], sz = new int[n + 1];
            int cnt = 0;
            order[cnt++] = 1;
            par[1] = 0;
            for (int i = 0; i < cnt; i++) {
                int x = order[i];
                for (int e = head[x]; e != -1; e = nxt[e]) {
                    int y = to[e];
                    if (y != par[x]) {
                        par[y] = x;
                        order[cnt++] = y;
                    }
                }
            }
            for (int i = n - 1; i >= 0; i--) {
                int x = order[i];
                sz[x]++;
                if (par[x] != 0) sz[par[x]] += sz[x];
            }
            int lo = 0, hi = n;
            int[] heavy = new int[n + 1];
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                Arrays.fill(heavy, 0);
                boolean ok = true;
                for (int i = 1; i < n && ok; i++) {
                    int x = order[i];
                    if (sz[x] > mid) {
                        int p = par[x];
                        heavy[p]++;
                        if (heavy[p] > (p == 1 ? 2 : 1)) ok = false;
                    }
                }
                if (ok) hi = mid;
                else lo = mid + 1;
            }
            sb.append(n - lo).append('\n');
        }
        System.out.print(sb);
    }
}
