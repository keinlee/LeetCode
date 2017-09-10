#筛选大城市

SELETE name,population,area
FROM World
WHERE area > 3000000 OR population > 25000000;



#另一种更高效率方法

SELETE name,population,area
FROM World
WHERE area>3000000
UNION
SELETE name,population,area
FROM World
WHERE population>25000000;
