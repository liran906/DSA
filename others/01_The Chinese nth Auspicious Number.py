"""
Problem: The Chinese nth Auspicious Number

IT5001 AY2020/21 Semester 1 Practical Exam (Old) Q3

In Chinese culture, the numbers 8 and 9 are considered auspicious:
- 8 sounds like "prosper" (发), symbolizing wealth and success.
- 9 sounds like "long-lasting" (久), symbolizing longevity.

We define an "auspicious number" as a positive integer consisting of only digits 8 and 9,
such as: 8, 9, 88, 89, 98, 99, 888, 889, ...

These auspicious numbers are arranged in increasing numerical order to form an infinite sequence.

Your task is to implement the following function:
    def nthAuspiciousNum(n):

Input:
- An integer n (1 ≤ n ≤ very large), representing the position in the sequence.

Output:
- Return the n-th auspicious number as an integer.

Examples:
>>> nthAuspiciousNum(1)
8
>>> nthAuspiciousNum(2)
9
>>> nthAuspiciousNum(3)
88
>>> nthAuspiciousNum(10)
899
>>> nthAuspiciousNum(59)
99988
"""

# O(n)
def nthAuspiciousNum(n):
    # Initialize a queue with the first two auspicious numbers as strings
    queue = ['8', '9']
    count = 0

    # Perform a level-order (BFS) traversal over the tree of auspicious numbers
    while queue:
        # Pop the front number from the queue
        num = queue.pop(0)
        count += 1

        # If we have reached the n-th number, return it as an integer
        if count == n:
            return int(num)

        # Generate the next two auspicious numbers by appending '8' and '9'
        # and enqueue them for future processing
        queue.append(num + '8')
        queue.append(num + '9')


# O(log n)
def nthAuspiciousNum(n):
    # This function calculates how many digits are needed to reach the n-th number.
    # Since each digit doubles the total count (2^d strings of length d),
    # we find the smallest 'lognum' such that total count up to that level covers n.
    def getLog(n):
        res = 0
        log = 1
        while log < n:
            log *= 2
            res += 1
        return res

    # Recursive helper to build the n-th auspicious number of length 'lognum'
    def helper(n, lognum):
        # Base case: single digit
        if lognum == 1:
            if n == 1:
                return '8'
            return '9'

        # Total number of strings with length lognum is 2^lognum
        # Left half starts with '8', right half with '9'

        # If n is within the left half (those starting with '8'):
        if n < 3 * 2 ** (lognum - 1) - 1:
            return '8' + helper(n - 2 ** (lognum - 1), lognum - 1)
        else:
            # Otherwise, it's in the right half (those starting with '9')
            return '9' + helper(n - 2 ** lognum, lognum - 1)

    # Calculate how many digits are needed to cover at least n values
    lognum = getLog(n / 2 + 1)

    # Recursively construct the number and convert to int
    return int(helper(n, lognum))


# O(log n)
# Same method but with math package.
def nthAuspiciousNum(n):
    import math
    def helper(n, lognum):
        if lognum == 1:
            if n == 1:
                return '8'
            return '9'
        if n < 3 * 2 ** (lognum - 1) - 1:
            return '8' + helper(n - 2 ** (lognum - 1), lognum-1)
        else:
            return '9' + helper(n - 2 ** lognum, lognum-1)

    lognum = math.ceil(math.log(n/2+1, 2))
    return int(helper(n, lognum))


# O(log n)
def nthAuspiciousNum(n):
    result = ''
    while n > 0:
        # 将 n-1 看作是“吉利二进制树”中的索引（从0开始）
        # 如果当前是奇数位置，说明它是某个父节点的左子（编码为 '8'）
        # 如果当前是偶数位置，说明它是右子（编码为 '9'）
        if n % 2 == 1:
            result = '8' + result
        else:
            result = '9' + result
        # 进入上一层节点（向上移动树的层级）
        n = (n - 1) // 2
    # 将构造出的字符串转为整数返回
    return int(result)

# 示例：输出第 4 个吉利数字
print(nthAuspiciousNum(4))  # 输出：89