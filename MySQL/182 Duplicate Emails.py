#重复的邮件

SELECT Email from Person GROUP BY Email HAVING COUNT(*)>1


#方法二：
SELECT DISTINCT a.Email
FROM Person a JOIN Person b
ON (a.Email = b.Email)
WHERE a.Id <> b.Id
'''
方法一：

group by ... having... 联合起来查询不重复的数据
having一般跟在group by之后，执行记录组选择的一部分来工作的
where则是执行所有数据来工作的

方法二：
FROM table1 INNER|LEFT|RIGHT JOIN table2 ON conditiona
join 用于多表中字段之间的联系
'''

#DISTINCT与GROUP BY的区别还有a.Email不太明白


