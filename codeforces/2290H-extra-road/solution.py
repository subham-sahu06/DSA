import sys
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(data[idx]); v = int(data[idx + 1]); idx += 2
            g[u].append(v)
            g[v].append(u)
        par = [0] * (n + 1)
        order = [1]
        for x in order:
            for y in g[x]:
                if y != par[x]:
                    par[y] = x
                    order.append(y)
        sz = [1] * (n + 1)
        for i in range(n - 1, 0, -1):
            x = order[i]
            sz[par[x]] += sz[x]
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            heavy = [0] * (n + 1)
            ok = True
            for i in range(1, n):
                x = order[i]
                if sz[x] > mid:
                    p = par[x]
                    heavy[p] += 1
                    if heavy[p] > (2 if p == 1 else 1):
                        ok = False
                        break
            if ok:
                hi = mid
            else:
                lo = mid + 1
        out.append(n - lo)
    print("\n".join(map(str, out)))
main()
