import sys
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        p = [0] * n
        ok = True
        for v in range(1, n + 1):
            i = int(data[idx]) + n - v
            idx += 1
            if not ok:
                continue
            if i < 0 or i >= n or p[i]:
                ok = False
            else:
                p[i] = v
        out.append(" ".join(map(str, p)) if ok else "-1")
    print("\n".join(out))
main()
