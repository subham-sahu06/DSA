import sys
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx + 1]); idx += 2
        pre = [0] * (n + 1)
        total = 0
        for i in range(1, n + 1):
            lo = max(1, i - k)
            g = 1 if pre[i - 1] ^ pre[lo - 1] == 0 else 0
            pre[i] = pre[i - 1] ^ g
            if int(data[idx + i - 1]) & 1:
                total ^= g
        idx += n
        out.append("Alice" if total else "Bob")
    print("\n".join(out))
main()
