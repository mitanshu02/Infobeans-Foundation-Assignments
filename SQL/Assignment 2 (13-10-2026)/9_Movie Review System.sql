-- QNO 9:You are designing a system to store movie reviews. Start with basic details and then evolve the table structure using ALTER, RENAME, TRUNCATE, and DROP, and perform INSERT operations at each stage.

-- Initial Table Creation:
-- Create a table movie_reviews with the following columns:
-- review_id INT
-- movie_title VARCHAR(150)
-- reviewer_name VARCHAR(100)
-- rating DECIMAL(2,1)
-- review_text TEXT

create table movie_review(
	review_id int,
    movie_title varchar(150),
    reviewer_name varchar(100),
    rating decimal(2,1),
    review_text text
    );
    
-- Insert 3 sample movie reviews

insert into movie_review values 
	(1,"Singham","Pankaj",7.8,"It was a good movie with lots of action"),
    (2,"Bahubali : The Beginning","Shikha",9.1,"A good action movie with lots of Goosebumps."),
    (3,"Avenger : Infinity War","Pappu",9.5,"Maza aa gya Iron Man ka Action Dekh Kar, ekdum Jhakaaaassss...");
    
select * from movie_review;

-- Step 1: Add More Columns (ALTER)
-- Add the following columns using ALTER:
-- review_date DATE
-- platform VARCHAR(50) — (e.g., IMDb, Rotten Tomatoes)
-- likes INT

alter table movie_review add column review_date date, add column platform varchar(50), add column likes int;
desc movie_review;

-- Insert 2 more rows with new columns

insert into movie_review values
    (4,"Drishyam","Soham",8.2,"Good movie, suspance and drama","2025-10-21","Netflix",1056),
    (5,"Toofaan","Bablu",9.8,"Ekdum mast, Big-b ne kya acting ki he yrr.","2026-04-01","Hotstar",10001);
    
select * from movie_review;

-- Step 2: Rename a Column
-- Rename the column reviewer_name to critic_name

alter table movie_review rename column reviewer_name to critic_name; 

-- Step 3: Modify Column Types
-- Modify:
-- rating to DECIMAL(3,1)
-- movie_title to VARCHAR(200)

alter table movie_review modify column rating decimal(3,1),
	modify column movie_title varchar(200);
    
-- Step 4: Drop an Unnecessary Column
-- Drop the likes column

alter table movie_review drop likes;

-- Step 5: Truncate the Table
-- Truncate the table so all data is removed

truncate table movie_review;
select * from movie_review;

-- Step 6: Rename the Table
-- Rename movie_reviews to archived_reviews

alter table movie_review rename to archived_reviews;

-- Step 7: Drop the Table
-- Finally, drop the archived_reviews table

drop table archived_reviews;
show tables;