
-- ASSIGNMENT 3 – PRODUCT MANAGEMENT SYSTEM

-- Q1. Create a database named shop_db and use the database.

create database if not exists shop_db;

use shop_db;


-- Q2. Create a table named product with the given columns.

create table product(
    product_id int auto_increment primary key,
    product_name varchar(50),
    category varchar(50),
    brand varchar(50),
    price int,
    quantity int
);


-- Q3. Insert the following 10 product records.

insert into product (product_name, category, brand, price, quantity)
values
("Laptop", "Electronics", "Dell", 55000, 10),
("Smartphone", "Electronics", "Samsung", 25000, 15),
("Keyboard", "Accessories", "Logitech", 1500, 25),
("Mouse", "Accessories", "HP", 800, 30),
("Monitor", "Electronics", "LG", 18000, 12),
("Headphones", "Accessories", "Sony", 3000, 20),
("Printer", "Electronics", "Canon", 12000, 8),
("Tablet", "Electronics", "Lenovo", 22000, 14),
("Webcam", "Accessories", "Logitech", 2500, 18),
("Speaker", "Accessories", "JBL", 4500, 16);


-- Q4. Display the structure of the product table using DESC.

desc product;


-- Q5. Display all records from the product table.

select * from product;
