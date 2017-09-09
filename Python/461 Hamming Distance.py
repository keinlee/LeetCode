#汉明距离

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #对两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离。
        #bin()是字符串类型
        return bin(x^y).count('1')
