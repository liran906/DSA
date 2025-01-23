# Products of Array Except Self
# https://neetcode.io/problems/products-of-array-discluding-self
# med

class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        if 0 not in nums:
            product = 1
            for n in nums:
                product *= n
            output = []
            for n in nums:
                output.append(int(product / n))
        else:
            count = 0 # counter of 0
            product = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    count += 1
                    pos = i # position of 0
                else:
                    product *= nums[i]
                output = [0 for i in nums]
            if count == 1:
                output[pos] = product
        return output

        