#列阵分区1

#runtime:32ms
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

#第二种方法
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[i] for i in range(len(nums)) if i % 2 == 0)

'''
sum()求和函数
sorted()排序函数，与sort的区别：
sort是列表成员函数，list.sort(),更改原列表顺序
sorted是内建函数，生成一个新的顺序列表，原列表不变
[::2]是列表分片：
[开始位置:结束位置:步长]
步长为2代表每前进2个元素取一个元素

第二种方法中是for...if...构建满足if条件的列表，if可以省略
[对(x)的操作 for x in 集合 if 条件]

嵌套
[对(x,y)的操作
for x in 集合1 
for y in 集合2 if 条件]
'''
