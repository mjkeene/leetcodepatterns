class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # [0, 1, 1, 2, 3, 5, 8, 13, 21, ...]
        arr = [0, 1]
        for i in range(2, n+1):
            arr.append(arr[i-2] + arr[i-1])
        return arr[n]

   """Optimized fibonacci, minimal memory usage"""
    # a, b = 0, 1
    # for i in range(2, n):
    #     c = a + b
    #     a = b
    #     b = c
    # return a + b

    """2**n runtime"""
    # if i == 0:
    #     return 0
    # if i == 1:
    #     return 1
    #
    # return fibonacci_bad(i - 1) + fibonacci_bad(i - 2)