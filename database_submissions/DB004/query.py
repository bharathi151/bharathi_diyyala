Q1="SELECT fname,lname FROM Actor WHERE id IN(SELECT pid FROM Cast WHERE mid=1000);"
Q2="SELECT count(mid) FROM Cast WHERE pid in(SELECT id FROM Actor WHERE fname='Harrison (I)' AND lname='Ford');"
Q3="SELECT DISTINCT pid FROM Cast WHERE mid in(SELECT id FROM Movie WHERE instr(name,'Harry Potter')>0);"
Q4="SELECT COUNT(DISTINCT pid) FROM Cast WHERE mid in(SELECT id FROM Movie WHERE year BETWEEN 1990 AND 2000);"