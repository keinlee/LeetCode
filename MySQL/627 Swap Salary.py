#交换薪水

#普通第一种写法 if 条件语句

UPDATE salary SET sex = IF(sex='f','m','f');


#普通第二种写法 case when

UPDATE salary SET sex = (CASE WHEN sex='f' 
                         THEN 'm'
                         ELSE 'f'
                         END);

#高级的写法 异或

UPDATE salary SET sex = CHAR(ASCII('f') ^ ASCII('m') ^ASCII(sex));

'''
解析一下第三种方法：
ASCII()函数在MySQL中，表示 返回字符串str的第一个字符的ASCII值
CHAR()函数在MYSQL中，表示 返回由参数对应的ASCII代码字符组成的一个字符串
SELECT ASCII('f')  -->102
SELECT ASCII('m')  -->109
SELECT 102^109  -->11
SELECT 11^102  -->109
SELECT 11^109  -->102

思路就是 m^m=0 f^f=0 0^f=f 0^m=m
利用异或的特性来返回不同的值，用于两者交换
'''