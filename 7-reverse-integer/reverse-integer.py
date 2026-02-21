class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = str(x * -1)
            op = int(res[::-1]) * -1
        else:
            res = str(x)
            op = int(res[::-1])
        if op < -2**31 or op > 2**31 - 1:
            return 0
        else:
            return op
