import sys
import bisect

input = sys.stdin.readline

n, q = map(int, input().split())
s = input().strip()

ops_l = []
ops_r = []
len_before = []
len_after = []

cur_len = n

for _ in range(q):
    t = input().split()

    if t[0] == '1':
        l, r = map(int, t[1:])
        ops_l.append(l)
        ops_r.append(r)
        len_before.append(cur_len)
        cur_len += (r - l + 1)
        len_after.append(cur_len)

    else:
        i = int(t[1])

        hi = len(len_after)

        while i > n:
            idx = bisect.bisect_left(len_after, i, 0, hi)

            if i > len_before[idx]:
                seg_len = ops_r[idx] - ops_l[idx] + 1
                i -= seg_len
                hi = idx
            else:
                hi = idx

        print(s[i - 1])
