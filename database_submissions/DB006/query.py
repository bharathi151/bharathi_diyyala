Q1="SELECT AVG(age) FROM Player;"

Q2="SELECT match_no,play_date FROM Match WHERE audience>50000 ORDER BY match_no ASC;"

Q3="SELECT t.team_id,count(t.win_lose)AS c FROM MatchTeamDetails AS t where t.win_lose='W' GROUP BY t.team_id ORDER BY c DESC,t.team_id ASC;"

Q4="SELECT m.match_no,m.play_date FROM Match AS m WHERE m.stop1_sec>(SELECT AVG(m1.stop1_sec) FROM Match as m1)ORDER BY m.match_no DESC;"

Q5="SELECT m.match_no,t.name,p.name FROM Match AS m1 INNER JOIN MatchCaptain AS m ON m1.match_no=m.match_no INNER JOIN Team AS t ON t.team_id=m.team_id INNER JOIN Player AS p ON p.player_id=m.captain ORDER BY m1.match_no ASC,t.name ASC;"

Q6="SELECT m.match_no,p.name,p.jersey_no FROM Match AS m INNER JOIN Player AS p ON p.player_id=m.player_of_match GROUP BY m.match_no ORDER BY m.match_no ASC;"

Q7="SELECT t1.name,(SELECT AVG(p.age) FROM Player AS p INNER JOIN Team AS t ON p.team_id=t.team_id AND t.name=t1.name GROUP BY t.team_id)AS a FROM Team AS t1 WHERE a>26 ORDER BY t1.name ASC;"

Q8="SELECT p.name,p.jersey_no,p.age,COUNT(p.player_id)AS c  FROM Player AS p INNER JOIN GoalDetails AS g ON g.player_id=p.player_id WHERE p.age<=27 GROUP BY g.player_id HAVING(g.player_id)>=1 ORDER BY c DESC,p.name ASC;"

Q9="SELECT g.team_id,((COUNT(g.team_id)*100.0)/(SELECT COUNT(*) FROM GoalDetails AS g1))FROM GoalDetails AS g GROUP BY g.team_id HAVING COUNT(g.team_id)>=1;"

Q10="SELECT AVG(c)FROM (SELECT COUNT(*)AS c FROM GoalDetails GROUP BY team_id);"

Q11="SELECT p.player_id,p.name,p.date_of_birth FROM Player AS p WHERE p.player_id NOT IN(SELECT g.player_id FROM GoalDetails AS g) ORDER BY p.player_id ASC;"

Q12="SELECT t.name,m.match_no,m.audience,m.audience-(SELECT AVG(m1.audience)FROM Match m1 INNER JOIN MatchTeamDetails AS mtd ON mtd.match_no=m1.match_no AND mtd.team_id=t.team_id GROUP BY mtd.team_id)FROM Team AS t INNER JOIN MatchTeamDetails AS mtd1 ON mtd1.team_id=t.team_id INNER JOIN Match AS m ON m.match_no=mtd1.match_no ORDER BY m.match_no ASC;"