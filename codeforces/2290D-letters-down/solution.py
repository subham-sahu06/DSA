import sys
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        diff = [0] * 27
        for i in range(n // 2):
            u, v = s[i] - 97, s[n - 1 - i] - 97
            if u > v:
                u, v = v, u
            if u < v:
                diff[u + 1] += 1
                diff[v + 1] -= 1
        cur = 0
        ans = 0
        for c in range(26):
            cur += diff[c]
            if cur > 0:
                ans += 1
        out.append(str(ans))
    print("\n".join(out))
main()
