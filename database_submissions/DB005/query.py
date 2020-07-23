Q1="""SELECT COUNT(id) FROM Movie WHERE year<1980;"""

Q2="""SELECT AVG(rank) FROM Movie WHERE year=1991;"""

Q3="""SELECT MIN(rank) FROM Movie WHERE year=1991;"""

Q4="""SELECT fname,lname FROM Actor WHERE id IN (SELECT pid FROM Cast WHERE mid=1002);"""

Q5="""SELECT COUNT(mid) FROM Cast WHERE pid IN (
    SELECT id FROM Actor WHERE fname='Orlando' AND lname='Galindo');"""
    
Q6="SELECT name FROM Movie WHERE name LIKE 'Harry Potter%' AND year between 2006 AND 2008;"

Q7="""SELECT DISTINCT fname,lname FROM Director WHERE id IN (
    SELECT DISTINCT did FROM MovieDirector WHERE mid in(SELECT DISTINCT id FROM Movie WHERE name LIKE 'Harry Potter%'));"""

Q8="""select m.name from Movie as m where m.id in(
    select md.mid from MovieDirector as md where md.did in(
        select id from Director where fname='Jackie (I)' and lname='Chan')) and m.id in (
    select mid from Cast where pid in (
        select id from Actor where fname='Jackie (I)' and lname='Chan')) 
        order by m.name asc;"""

Q9="""select d.fname,d.lname from Director as d 
    inner join MovieDirector on did=d.id 
        inner join Movie as m on m.year=2001 and mid=m.id 
            group by d.id having count(d.id)>=4 
    order by fname asc,lname desc;"""

Q10="""SELECT DISTINCT * FROM Actor WHERE id NOT IN (
SELECT pid FROM Cast WHERE mid IN (
SELECT id FROM Movie WHERE year between 1990 and 2000))
ORDER BY id DESC LIMIT 100;"""

Q11="""select gender,100.0*count(gender)/(select count(id) from actor) as p from Actor Group BY gender order  by p desc;"""

Q12="""select m.name,m1.name,m.year,m.rank from Movie as m 
inner join Movie as m1 on m.id<m1.id and m.year=m1.year and m.rank=m1.rank 
order by m.name asc limit 100;"""

Q13="""select a.fname,m.year,avg(m.rank) from Actor as a 
inner join Cast as c on c.pid=a.id inner join Movie as m 
on m.id=c.mid group by a.id,m.year
order by a.fname asc,m.year desc limit 100;"""

Q14="""select d.fname,m.name from Director as d 
inner join MovieDirector as md on d.id=md.did 
inner join Movie as m on m.id=md.mid 
group by md.did,md.mid having m.rank=max(m.rank) order by m.name limit 100;"""

Q15="""select distinct d.id,d.fname from Director as d 
where d.id not in (select did from MovieDirector where mid in (
    select m.id from Movie as m where year<2005)) and d.id in (
        select did from MovieDirector where mid in (
            select m.id from Movie as m where year>2005)) 
            order by d.id;"""
            
Q16="""select a.fname,d.fname,avg(m.rank) as ranks from actor as a 
inner join cast as c on a.id=c.pid inner join movie as m on c.mid=m.id 
inner join moviedirector as md on md.mid=m.id 
inner join director as d on d.id=md.did group by d.id,c.pid 
having count(md.did)>=5 and count(c.pid)>=5 
order by ranks desc,d.fname asc,a.fname desc limit 100;"""