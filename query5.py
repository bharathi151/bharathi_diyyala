Q1="SELECT fname,lname FROM Actor WHERE id IN(SELECT pid FROM Cast WHERE mid=1000);"
Q2="SELECT count(mid) FROM Cast WHERE pid in(SELECT id FROM Actor WHERE fname='Harrison (I)' AND lname='Ford');"
Q3="SELECT DISTINCT pid FROM Cast WHERE mid in(SELECT id FROM Movie WHERE instr(name,'Harry Potter')>0);"
Q4="SELECT COUNT(DISTINCT pid) FROM Cast WHERE mid in(SELECT id FROM Movie WHERE year>=1990 AND year<=2000);"
#Get all the actors first and last names for movie_id = 1000
#Count number of movies in which actor “Harrison (I) Ford” acted
#first name: “Harrison (I)”
#last name: “Ford”
#Get all the distinct actors ids who acted in all ‘Harry Potter’ movies.
#How many distinct actors have acted in any movie between 1990 and 2000.
#q1=select fname,lname from Actor inner join Cast on pid=id and mid=1000;
#q2=select count(mid) from Cast inner join Actor on pid=id and fname='Harrison (I)' and lname='Ford';
#q3=select distinct pid from Cast inner join Movie on id=mid and instr(name,'Harry Potter')>0;
#q4=select count(distinct pid) from Cast inner join Movie on mid=id and year between 1990 and 2000;
