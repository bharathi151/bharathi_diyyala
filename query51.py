Q1="SELECT COUNT(id) FROM Movie WHERE year<1980;"
Q2="SELECT round(AVG(rank),4) FROM Movie WHERE year=1991;"
Q3="SELECT MIN(rank) FROM Movie WHERE year=1991;"
Q4="SELECT fname || ' ' || lname FROM Actor WHERE id in(SELECT pid FROM Cast WHERE mid=1002);"
Q5="SELECT COUNT(mid) FROM Cast WHERE pid in(SELECT id FROM Actor WHERE fname='Orlando' AND lname='Galindo');"
Q6="SELECT name FROM Movie WHERE name LIKE 'Harry Potter%' AND year between 2006 AND 2008;"
Q7="SELECT DISTINCT fname,lname FROM Director WHERE id in (SELECT DISTINCT did FROM MovieDirector WHERE mid in(SELECT DISTINCT id FROM Movie WHERE name LIKE 'Harry Potter%'));"
Q8="SELECT * FROM Movie WHERE id in(SELECT mid FROM MovieDirector WHERE did in(SELECT id FROM Actor WHERE fname='Jackie (I)' AND lname='Chan')) ORDER BY name ASC;"
#Q9="SELECT fname,lname FROM Director WHERE id in (SELECT did FROM MovieDirector WHERE mid in(SELECT id FROM Movie WHERE year=2001) AND COUNT(id)>=4)ORDER BY fname ASC OR ORDER BY lname DESC;"
Q10="SELECT DISTINCT * FROM Actor WHERE id NOT IN (SELECT pid FROM Cast WHERE mid in(SELECT id FROM Movie WHERE year between 1990 and 2000)) ORDER BY id DESC LIMIT 100;"
Q11="select 'M' ||' ' ||round(100.0*(select count(id) from actor where gender='M')/count(*),1) from actor;select 'F' ||' ' ||round(100.0*(select count(id) from actor where gender='F')/count(*),1) from actor;"
#Q12="SELECT fname,(SELECT year,(select AVG(ranks) from movie as m where m.id in (select mid from Cast where pid=id))) FROM Actor;"
Q13="select fname,(select year from movie order by year desc),(select avg(rank) from movie) from actor where id in (select pid from cast where mid in (select id from movie))order by fname asc LIMIT 100;"
List fname and lname of directors who directed at least 4 movies which released in 2001. Your query should return results in the following order [5 points]

ascending on fname
and then descending on lname

Write a query to get movie pairs in which both the movies are released in the same year and have same rating. Your query should result in 100 entires and sorted in ascending order of first movie name. [10 points]
Return only distinct pairs i.e pairs (Movie1, Movie2) and (Movie2, Movie1) should be considered as same.

Sample Output Format:

MovieName1 MovieName2 8 2000 
MovieName3 MovieName4 8 2001 

Rank of actor for a given year is the averge of ranks of all the movies he/she is casted in and released in that year. Your query should result fname, year and the rank of the actors. Your query should result in only 100 entires when ordered as following [10 points]

ascending order on actor fname and then
descending order on year
FROM(Director AS director INNER JOIN MovieDirector AS md on md.did=director.id) INNER JOIN Movie as movie ON movie.id=md.mid LIMIT 10;


SELECT avg_rank FROM(SELECT sq_director.id,avg(sq_movie.rank)as avg_rank FROM (Director as sq_director INNER JOIN MovieDirector as sq_md on sq_md.did=sq_director.id)INNER JOIN Movie as sq_movie ON sq_movie.id=sq_md.mid GROUP BY sq_director.id) limit 10;      

SELECT sq_md.did FROM MovieDirector AS sq_md INNER JOIN Movie AS sq_movie ON sq_md.mid=sq_movie.id AND sq_movie.year<2000 limit 10;    