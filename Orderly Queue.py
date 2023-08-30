# k = 3
# baaca move b
# aacab move c
# aaabc

# k = 3
# cbaaca move b
# caacab move c
# aacabc move c
# aaabcc

# if the (n+1)th chr is smaller than the any previous chr
# do the mv things
# 2 cases:
#   k = 3
#   acbaa -> acaab -> aaabc
#   acbaa -> abaac -> aaacb
# but what if it's acba only
#   acba -> acab -> aabc
#   acba -> abac -> aacb

# principle is to let the former chr as small as possible
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        pass

from collections import deque

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        left, right = s[:k], s[k:]
        max_left, min_right = max(left), min(right)
        
        while True:
            
            
            pass

# brute force log(n^2)

# baaca
# aacab
# aaabc

from collections import deque
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s_q = deque(s)
        i = 1
        while i <= k:
            min_chr = min(s_q[i-1:])
            while s_q[i-1] != min_chr:
                s_q.append(s_q.popleft())
            i += 1
        return ''.join(s_q)


# brute force log(n^2)

# baaca
# aacab
# aaabc

from collections import deque
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s_q = deque(s)
        def find_min(q, i):
            my_min = False
            for j in range(i, len(q)):
                if not my_min:
                    my_min = q[j]
                else:
                    if q[j] < my_min:
                        my_min = q[j]
            return my_min        
        i = 1
        while i <= k:
            min_chr = find_min(s_q, i-1)
            while s_q[i-1] != min_chr:
                s_q.append(s_q.popleft())
            i += 1
        return ''.join(s_q)
            


# brute force log(n^2)

# baaca
# aacab
# aaabc

from collections import deque
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s_q = deque(s)  

        i = 1
        output_list = []
        while i <= k:
            min_chr = min(s_q)
            while s_q[0] != min_chr:
                s_q.append(s_q.popleft())
                
            output_list.append(s_q.popleft())
            i += 1

        for s in s_q:
            output_list.append(s)

        return ''.join(output_list)
### failed at print(Solution().orderlyQueue("xmvzi", 2)) imvzx should be "imvxz"
# "xmvzi" k=2
s_list = []
for s in "xmvzi":
    s_list.append(ord(s))
print(s_list)
# [120, 109, 118, 122, 105]
# [105, 120, 109, 118, 122]
# [105, 109, 118, 122, 120]
print([chr(i) for i in [105, 109, 118, 122, 120]])
# which is ['i', 'm', 'v', 'z', 'x']

# "xmvzi"
# mvzix
# mzixv
# mixvz
# ixvzm
# imxvz

print(Solution().orderlyQueue("baaca", 3))
print(Solution().orderlyQueue("xmvzi", 2))
