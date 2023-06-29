
class Solution(object):
    '''nums = [2, 7, 11, 15]
    target = 9'''
    def TwoSum(self, nums, target):
        buff_dict = {}
        if(len(nums) < 2):
            return False
        else:
            for i in range(len(nums)):
                if nums[i] in buff_dict:
                    return [buff_dict[nums[i]],i]
                else:
                    buff_dict[target - nums[i]] = i

    TwoSum(0,[2, 7, 11, 15], 9)

'''
buff_dict巧妙地把nums数组的数值和索引转换了 方便最后输出索引值
遍历nums，将每一个值以 （目标值减去该nums的结果）：该nums的索引的形式计入buff_dict，继续遍历寻找匹配减法结果的值，再输出索引。
'''