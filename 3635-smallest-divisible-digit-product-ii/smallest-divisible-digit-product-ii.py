class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        x = t
        c2 = c3 = c5 = c7 = 0
        while x % 2 == 0:
            c2 += 1
            x //= 2
        while x % 3 == 0:
            c3 += 1
            x //= 3
        while x % 5 == 0:
            c5 += 1
            x //= 5
        while x % 7 == 0:
            c7 += 1
            x //= 7
        if x > 1:
            return "-1"

        def req(a, b, c, d):
            a, b, c, d = max(0, a), max(0, b), max(0, c), max(0, d)
            r2, r3 = a % 3, b % 2
            if not r2 and not r3:
                e = 0
            elif r2 == 2 and r3 == 1:
                e = 2
            else:
                e = 1 if (r2 or r3) else 0
            return c + d + a // 3 + b // 2 + e

        P = [(0, 0, 0, 0), (0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (2, 0, 0, 0), (0, 0, 1, 0), (1, 1, 0, 0), (0, 0, 0, 1), (3, 0, 0, 0), (0, 2, 0, 0)]
        N = len(num)
        pref = [(0, 0, 0, 0)] * (N + 1)
        p2 = p3 = p5 = p7 = 0
        z = N
        for idx, ch in enumerate(num):
            if ch == '0':
                z = idx
                break
            d = int(ch)
            v2, v3, v5, v7 = P[d]
            p2, p3, p5, p7 = p2 + v2, p3 + v3, p5 + v5, p7 + v7
            pref[idx + 1] = (p2, p3, p5, p7)

        if z == N:
            p2, p3, p5, p7 = pref[N]
            if p2 >= c2 and p3 >= c3 and p5 >= c5 and p7 >= c7:
                return num

        top_i = z if z < N else N - 1
        for i in range(top_i, -1, -1):
            p2, p3, p5, p7 = pref[i]
            rc2, rc3, rc5, rc7 = c2 - p2, c3 - p3, c5 - p5, c7 - p7
            start_d = 1 if num[i] == '0' else int(num[i]) + 1
            for d in range(start_d, 10):
                v2, v3, v5, v7 = P[d]
                n2, n3, n5, n7 = rc2 - v2, rc3 - v3, rc5 - v5, rc7 - v7
                rem = N - 1 - i
                if req(n2, n3, n5, n7) <= rem:
                    sol = list(num[:i]) + [str(d)]
                    cur2, cur3, cur5, cur7 = n2, n3, n5, n7
                    for r in range(rem - 1, -1, -1):
                        for w in range(1, 10):
                            w2, w3, w5, w7 = P[w]
                            if req(cur2 - w2, cur3 - w3, cur5 - w5, cur7 - w7) <= r:
                                sol.append(str(w))
                                cur2, cur3, cur5, cur7 = cur2 - w2, cur3 - w3, cur5 - w5, cur7 - w7
                                break
                    return "".join(sol)

        L = max(N + 1, req(c2, c3, c5, c7))
        sol = []
        cur2, cur3, cur5, cur7 = c2, c3, c5, c7
        for r in range(L - 1, -1, -1):
            for w in range(1, 10):
                w2, w3, w5, w7 = P[w]
                if req(cur2 - w2, cur3 - w3, cur5 - w5, cur7 - w7) <= r:
                    sol.append(str(w))
                    cur2, cur3, cur5, cur7 = cur2 - w2, cur3 - w3, cur5 - w5, cur7 - w7
                    break
        return "".join(sol)