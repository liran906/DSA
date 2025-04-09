"""
Problem: Medical Research Tests

IT5001 AY2024/25 Semester 1 Practical Exam 2 (Old)

In a hospital, a series of medical tests is scheduled for patients. Each test is uniquely labeled
from 1 to n, and the tests are arranged in a specific original order (a permutation of 1 to n).
For example, the original test schedule might be:

    (3, 5, 6, 4, 2, 1, 7)

However, due to a computer virus, some test records were deleted, leaving only a partial
subsequence of the original schedule, for example:

    (6, 4, 2, 1)

We are guaranteed that:
- The remaining test numbers are in the correct relative order (i.e., they form a subsequence).
- The total number of tests n is known.

Your task is:
Write a function:

    def original_schedule(n, reduced_schedule)

which returns the lexicographically smallest permutation of 1 to n such that `reduced_schedule` is
a subsequence of it.

Lexicographical order (dictionary order) means comparing tuples from left to right, and sorting
based on the first difference.

Example:
If n = 3 and reduced_schedule = (1, 3), the possible permutations that include (1, 3) are:
- (1, 2, 3)
- (1, 3, 2)
- (2, 1, 3)
- (3, 1, 2)

Among them, (1, 2, 3) comes first in lexicographical order, so it is the correct answer.

You must return the first (i.e., smallest in lexicographical order) permutation of length n
that contains the reduced_schedule as a subsequence.

Examples:
>>> original_schedule(7, (6, 4, 2, 1))
(3, 5, 6, 4, 2, 1, 7)

>>> original_schedule(5, (1, 4, 2))
(1, 3, 4, 2, 5)

>>> original_schedule(3, (1, 2))
(1, 2, 3)
"""

def original_schedule(n, reduced_schedule):
    """
    Attempt to reconstruct a full permutation of 1 to n by merging the reduced_schedule
    and missing elements in a greedy manner, such that the result is as lexicographically
    small as possible while preserving the order of reduced_schedule.

    Note: This is a greedy approach and works correctly only if inserting the missing
    elements in sorted order before/around reduced_schedule doesn't break the subsequence.

    Parameters:
        n (int): Total number of test records (original permutation length)
        reduced_schedule (tuple): Partial test records, in correct relative order

    Returns:
        tuple: A permutation of 1 to n that includes reduced_schedule as a subsequence,
               constructed greedily to be lexicographically small.
    """

    # Step 1: Compute which numbers are missing from the reduced schedule
    slist = set([i + 1 for i in range(n)])  # full set {1, 2, ..., n}
    lack = list(slist - set(reduced_schedule))  # missing values (to be inserted)

    # Step 2: Merge 'lack' and 'reduced_schedule' in lexicographical order
    # while preserving the relative order of reduced_schedule
    res = []
    lp, rp = 0, 0  # pointers for lack[] and reduced_schedule[]

    while lp < len(lack) and rp < len(reduced_schedule):
        if lack[lp] < reduced_schedule[rp]:
            res.append(lack[lp])
            lp += 1
        else:
            res.append(reduced_schedule[rp])
            rp += 1

    # Step 3: Append any remaining elements
    res += lack[lp:]
    res += reduced_schedule[rp:]

    # Return as a tuple
    return tuple(res)

print(original_schedule(7,(6,4,2,1))) #(3, 5, 6, 4, 2, 1, 7)

print(original_schedule(5,(1,4,2))) #(1, 3, 4, 2, 5)

print(original_schedule(3,(1,2))) 



# over complicated!!
def original_schedule(n, reduced_schedule):
    """
    Given a reduced test schedule (a subsequence of the original one) and total number of tests n,
    return the lexicographically smallest full permutation of 1 to n that includes reduced_schedule
    as a subsequence.

    Parameters:
        n (int): total number of tests (i.e., length of the full schedule)
        reduced_schedule (tuple): partial subsequence of the original schedule

    Returns:
        tuple: the lexicographically smallest permutation of 1..n containing reduced_schedule
    """

    def helper(lst, used):
        """
        Recursively builds all permutations of 1 to n using backtracking.
        Once a full permutation is built (length == n), checks if it contains
        reduced_schedule as a subsequence using `jackpot()`.

        Parameters:
            lst (list): current permutation being built
            used (list of bool): tracks whether a number has been used

        Returns:
            tuple or None: the first valid permutation found, or None if not found yet
        """
        # Base case: full permutation formed
        if len(lst) == n:
            if jackpot(lst, reduced_schedule):
                return tuple(lst)
            return

        # Try each number from 1 to n
        for i in range(n):
            if not used[i]:
                used[i] = True
                lst.append(i + 1)
                res = helper(lst, used)
                if res:  # if a valid result is found, bubble it up
                    return res
                lst.pop()
                used[i] = False

    def jackpot(lst, expect):
        """
        Checks if 'expect' is a subsequence of 'lst'.

        Parameters:
            lst (list): full permutation
            expect (tuple): reduced_schedule that must be a subsequence

        Returns:
            bool: True if expect is a subsequence of lst, False otherwise
        """
        check = lst
        for i in expect:
            if i in check:
                idx = check.index(i)
                check = check[idx + 1:]  # move to next part after matched element
            else:
                return False
        return True

    # Start DFS search with empty permutation and all unused numbers
    return helper([], [False] * n)