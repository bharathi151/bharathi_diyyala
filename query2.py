Q1="SELECT * FROM Movie ORDER BY rank DESC LIMIT 10;"
Q2="SELECT * FROM Movie ORDER BY rank DESC LIMIT 10 OFFSET 10;"
Q3="SELECT name FROM Movie WHERE year>2006;"
Q4="SELECT name FROM Movie WHERE rank<1.1;"
Q5="SELECT * FROM Movie WHERE year>=2005 AND year<=2007;"
Q6="SELECT name,year FROM Movie WHERE instr(name,'Harry Potter')>0;"
Q7="SELECT * from Actor WHERE fname='Christin' and instr(lname,'Watson')<=0;"
Q8="SELECT * from Actor WHERE fname='Christin' and lname='Watson';"
Q9="SELECT name FROM Movie WHERE year=1990 AND rank=5;"
Q10="SELECT * FROM Actor WHERE fname='Christin' OR lname='Watson';"
Q11="SELECT name FROM Movie WHERE year>=2007 AND year<=2009;"
Q12="SELECT DISTINCT year FROM Movie ORDER BY year ASC;"
Q13="SELECT * FROM Actor WHERE fname='Christin' OR lname='Watson' AND gender='M' ORDER BY fname ASC;"
