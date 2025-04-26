# https://leetcode.cn/problems/3sum/
# m

class Solution(object):
    def threeSum(self, nums):
        # 排序，这样才能用指针法
        nums.sort()
        res, n = [], len(nums)
        # a b c 三个指针，大小关系是 0 <= a < b < c < len(nums)
        for a in range(n-2):
            # 因为题目要求不重复，所以如果有重复的 a，直接跳过
            if a > 0 and nums[a] == nums[a-1]:
                continue

            # 确定需要的 nums[b] 和 nums[c] 之和
            target = -nums[a]
            b, c = a + 1, n - 1
            # 开始双指针遍历，只有排序后才能这么干
            while b < c:
                if nums[b] + nums[c] > target:
                    c -= 1
                elif nums[b] + nums[c] < target:
                    b += 1
                elif nums[b] + nums[c] == target:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1 # 这一句也是同理，不写也能通过，但写了更好
                    # 成功匹配后，为了保证答案去重：下一个 nums[b] 必须是不同的数
                    while b < c and nums[b] == nums[b-1]:
                        b += 1
                    
                    # 同理，但如果有 b 不重复，这段关于 c 的循环不写也没问题，会在上面的循环迭代
                    while b < c and nums[c] == nums[c+1]:
                        c -= 1
        return res

s = Solution()
print(s.threeSum([-2, 0, 0, 0, 2, 2]))