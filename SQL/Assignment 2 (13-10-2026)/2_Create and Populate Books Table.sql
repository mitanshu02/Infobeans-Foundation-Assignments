-- QNO  2: Create and Populate books Table
-- Columns:

-- book_id INT

-- title VARCHAR(150)

-- author VARCHAR(100)

-- genre VARCHAR(50)

-- publication_year INT

-- price DECIMAL(6,2)

-- publisher VARCHAR(100)

-- Task:

-- Insert 4 book records.

create table books(
	book_id int,
	title varchar(150),
	author varchar(100),
	genre varchar(50),
	publication_year int,
	price decimal(6,2),
	publisher varchar(100)
);

desc books;

insert into books values
	(1,"Python","abc","Educational",2005,145.00,"Shiksha Books"),
    (2,"How to win friends","James","Self help",1945,165.00,"American Books"),
    (3,"Rich Dad Poor Dad","Richard","Finance",1988,226.99,"American Books"),
    (4,"Can't Hurt Me","David Goggins","Autobiography",2001,450.00,"Star Books"),
    (5,"Fundamentals of Programming","William","Educational",2009,750.00,"Shiksha Books");
    
select * from books;