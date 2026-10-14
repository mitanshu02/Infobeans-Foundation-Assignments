-- QNO  3: ALTER students Table
-- Task:

-- Add a column dob DATE
alter table students add column dob date;
desc students;

-- Rename column phone to mobile_number
alter table students rename column phone to mobile_number;

-- Modify column age to SMALLINT
alter table students modify column age smallint;

-- Drop column email
alter table students drop column email;