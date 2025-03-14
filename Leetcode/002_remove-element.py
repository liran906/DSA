# https://leetcode.cn/problems/remove-element/
# e
'''
左右指针
分别往中间遍历,左指针遇到等于 val 的值时就和右指针互换(此时右指针不能等于 val)
当左右指针相遇,就是遍历结束,返回任意指针即可
'''
class Solution(object):
    def removeElement(self, nums, val):
        i, r = 0, len(nums)
        while r > i: # i == r 时结束
            if nums[i] == val:
                r -= 1
                while r > i and nums[r] == val: # 右指针如果是 val，正好省的换了，r-=1
                    r -= 1
                nums[i], nums[r] = nums[r], nums[i] # i 和 r 互换
            else:
                i += 1
        return i

'''
快慢指针法 
fast 指向新数组(去掉等于val值后形成的数组)所需要的元素(也就是非 val 的元素),
slow 指向当前被替换的元素
也就是 fast 遍历一遍,把非 val 的值赋给slow,如果遇到和 val 相同的值就跳过
'''
class Solution(object):
    def removeElement(self, nums, val):
        fast, slow = 0, 0
        while fast < len(nums):
            while nums[fast] == val:
                fast += 1
                if fast >= len(nums):
                    return slow
            nums[slow] = nums[fast]
            fast += 1
            slow += 1
        return slow