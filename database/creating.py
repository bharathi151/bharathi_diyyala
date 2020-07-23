def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
def create_table():
	query=f"""
	CREATE TABLE {input()}(
		student_id INT,
		name  VARCHAR(100),
		age INT
	)"""
	write_data(query)   
def table():
	query=f"""
	CREATE TABLE {input()} (
    id INT PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);
"""
	write_data(query)
def new_table():
	query=f"""
	CREATE TABLE {input()} (
    child_id INT,
    dog_id INT,
    FOREIGN KEY(child_id) REFERENCES child(id),
    FOREIGN KEY(dog_id) REFERENCES dog(id)
	);"""
def insert_data():
	for i in range(int(input())):
		table,id,name,age=input().split(',')
		query=f"""
		INSERT INTO {table} (student_id,name,age) VALUES({id},{name},{age});
		"""
		write_data(query)
def get_info():
	query=f"""
	SELECT * FROM {input()};
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info
	
def condition():
	query=f"""
	SELECT student_id,name,age FROM {input()} WHERE age>10;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info
def projection():
	query=f"""
	SELECT student_id,name,age-20 FROM {input()} WHERE student_id>5;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info
	
def union():
	query="""
	SELECT * FROM student UNION ALL SELECT * FROM student1;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info

def intersect():
	query="""
	SELECT * FROM student INTERSECT SELECT * FROM student1;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info
def difference():
	query="""
	SELECT * FROM student EXCEPT SELECT * FROM student1;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info
def product():
	query="""
	SELECT * FROM student CROSS JOIN student1;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info
def delete():
	id=1
	query=f"""
	DELETE FROM {input()} WHERE student_id={id};
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info

def count():
	query="""
	SELECT COUNT (*) FROM student WHERE age>11;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}")
	return info
def like():
	query="""
	SELECT * FROM student WHERE name LIKE 'a%';
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}	{info[i][2]}")
	return info
def avg():
	query="""
	SELECT AVG (age), COUNT(name) FROM student WHERE age>11;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}")
	return info
def max():
	query="""
	SELECT MAX (age), COUNT(age) FROM student;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}")
	return info
def min():
	query="""
	SELECT MIN (age), COUNT(age) FROM student;
	"""
	info=read_data(query)
	for i in range(len(info)):
		print(f"{info[i][0]}	{info[i][1]}")
	return info
