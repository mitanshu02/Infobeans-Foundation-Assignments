
-- ASSIGNMENT 2 – EMPLOYEE MANAGEMENT SYSTEM

-- Q1. Create a database named company_db and use the database.

create database if not exists company_db;

use company_db;


-- Q2. Create a table named employee with the given columns.

create table employee(
    employee_id int auto_increment primary key,
    employee_name varchar(50),
    age int,
    department varchar(50),
    designation varchar(50),
    salary int
);


-- Q3. Insert the following 10 employee records.

insert into employee (employee_name, age, department, designation, salary)
values
("Rahul Sharma", 28, "IT", "Developer", 55000),
("Priya Verma", 26, "HR", "Executive", 42000),
("Amit Singh", 30, "IT", "Team Lead", 75000),
("Neha Patel", 27, "Finance", "Accountant", 48000),
("Rohit Mehta", 32, "IT", "Manager", 90000),
("Sneha Jain", 25, "Marketing", "Executive", 40000),
("Karan Gupta", 29, "IT", "Developer", 60000),
("Pooja Mishra", 31, "HR", "Manager", 80000),
("Ankit Tiwari", 28, "Finance", "Analyst", 65000),
("Riya Kapoor", 27, "Marketing", "Manager", 70000);


-- Q4. Display the structure of the employee table using DESC.

desc employee;


-- Q5. Display all records from the employee table.

select * from employee;
