#结合两个表

SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
FROM Person 
LEFT JOIN Address 
ON Person.PersonID = Address.PersonId;


'''
LEFT JOIN 关键字会从左表 (table_name1) 那里返回所有的行，
即使在右表 (table_name2) 中没有匹配的行。

SELECT column_name(s)
FROM table_name1
LEFT JOIN table_name2 
ON table_name1.column_name=table_name2.column_name
'''