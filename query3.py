Q1="SELECT COUNT(year) FROM Movie WHERE year=1991;"
Q2="SELECT MAX(rank) FROM Movie;"
Q3="SELECT MIN(rank) FROM Movie WHERE year=2000;"
Q4="SELECT AVG(rank) FROM Movie WHERE year=2000;"
Q5="SELECT COUNT(year),year FROM Movie GROUP BY year ORDER BY year ASC;"
Q6="SELECT MIN(year),MAX(year) FROM Movie;"
Get the total number of movies that are released in year 1991
Get the least rank for a movies
Get the maximum rank for movies that are released in year 2000
Get the average ranking for movies that are released in year 2000
Get number of movies released for each year. (year, count) in ascending order of year
Find the time period that this database covers. (start year, end year)
