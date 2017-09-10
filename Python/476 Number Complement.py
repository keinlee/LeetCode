#补数

#方法一 38ms
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int('1'*(len(bin(num))-2),2)^num


#方法二 42ms
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=1
        while i<=num:
            i <<=1
        return (i-1)^num

'''
这题的主要思路是'111'的形式与num异或得出补数，num=5='0b101'

解析方法一：
由于Python中bin()函数得出的结果是'0b101'，所以算长度的时候得去掉2个长度
'0b0101'是不可能出现的，所以可以直接计算长度，不然还需要判断第一位是否为1
int()函数有两位参数，第二位参数代表进制，默认是10进制
如果int()函数有第二位参数，第一位参数必须是str字符串
'1'*3 得出的结果是'111'
1^1=0
1^0=1
0^0=0
0^1=1

方法二：
这个采用的是位移方法，从1开始每次二进制后面补个0，比原数多一位数，
最终的结果减去1也是得出来的是'111'的形式，类似与(2^n)-1
bin(7)='0b111'
'''
