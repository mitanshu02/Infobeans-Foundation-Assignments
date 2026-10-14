-- QNO  1: Create and Populate students Table
-- Columns:

-- id INT

-- name VARCHAR(100)

-- age INT

-- gender VARCHAR(10)

-- address VARCHAR(150)

-- phone VARCHAR(15)

-- email VARCHAR(100)

-- Task:

-- Insert 5 different student records with dummy data.


mysql> create table students(
    -> id int,
    -> age int,
    -> gender varchar(10),
    -> address varchar(150),
    -> phone varchar(15),
    -> email varchar(100)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> desc students;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| id      | int          | YES  |     | NULL    |       |
| age     | int          | YES  |     | NULL    |       |
| gender  | varchar(10)  | YES  |     | NULL    |       |
| address | varchar(150) | YES  |     | NULL    |       |
| phone   | varchar(15)  | YES  |     | NULL    |       |
| email   | varchar(100) | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
6 rows in set (0.01 sec)

mysql> insert into students values(
    -> 1,21,"Male","Indore","9926505364","pappu@gmail.com"),
    -> (2,25,"Female","Bhopal","8787989856","shanu@gmail.com"),
    -> (3,16,"Male","Gwalior","9945658512","Harish@gmail.com"),
    -> (4,19,"Female","Chennai","7845789565","Urmila@gmail.com"),
    -> (5,20,"Female","Riwa","9832657454","Era@gmail.com");
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from students;
+------+------+--------+---------+------------+------------------+
| id   | age  | gender | address | phone      | email            |
+------+------+--------+---------+------------+------------------+
|    1 |   21 | Male   | Indore  | 9926505364 | pappu@gmail.com  |
|    2 |   25 | Female | Bhopal  | 8787989856 | shanu@gmail.com  |
|    3 |   16 | Male   | Gwalior | 9945658512 | Harish@gmail.com |
|    4 |   19 | Female | Chennai | 7845789565 | Urmila@gmail.com |
|    5 |   20 | Female | Riwa    | 9832657454 | Era@gmail.com    |
+------+------+--------+---------+------------+------------------+
5 rows in set (0.00 sec)
