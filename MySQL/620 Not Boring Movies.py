#不枯燥的电影

SELECT * FROM cinema
WHERE (id % 2 = 1) AND DESCRIPTION <> 'boring'
ORDER BY rating DESC;

'''
id%2=1 可以用mod(id,2)来代替
MySQL里面不等号标准的是<>而不是!=
'''
