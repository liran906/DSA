# https://leetcode.cn/problems/4sum-ii/
# m

class Solution(object):
    '''
    https://leetcode.cn/problems/4sum-ii/solutions/65894/chao-ji-rong-yi-li-jie-de-fang-fa-si-shu-xiang-jia/
    '''
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        dct = dict()
        for n1 in nums1:
            for n2 in nums2:
                dct[n1+n2] = dct.get(n1+n2, 0) + 1

        res = 0
        for n3 in nums3:
            for n4 in nums4:
                target = -n3 - n4
                res += dct.get(target, 0)
        
        return res