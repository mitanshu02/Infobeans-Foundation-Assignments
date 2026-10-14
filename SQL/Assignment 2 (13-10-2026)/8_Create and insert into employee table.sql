-- QNO  8: Create and Insert into employees Table
-- Columns:

-- emp_id INT

-- emp_name VARCHAR(100)

-- gender VARCHAR(10)

-- dob DATE

-- department VARCHAR(100)

-- position VARCHAR(100)

-- salary DECIMAL(8,2)

-- joining_date DATE

-- phone VARCHAR(15)

-- Task:

-- Insert 5 employee records

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    gender VARCHAR(10),
    dob DATE,
    department VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(8,2),
    joining_date DATE,
    phone VARCHAR(15)
);

INSERT INTO employees(emp_id, emp_name, gender, dob, department, position,salary, joining_date, phone)
VALUES
    (1, 'Aarav Sharma', 'Male', '2000-05-15', 'IT','Software Developer', 55000.00, '2023-07-10', '9876543210'),
    (2, 'Priya Verma', 'Female', '1999-11-22', 'HR','HR Executive', 42000.00, '2022-03-15', '9876543211'),
    (3, 'Rahul Patel', 'Male', '2001-02-08', 'Finance','Accountant', 38000.50, '2024-01-08', '9876543212'),
    (4, 'Neha Gupta', 'Female', '1998-08-30', 'IT','Data Analyst', 62000.75, '2021-09-20', '9876543213'),
    (5, 'Vikram Singh', 'Male', '2000-12-12', 'Marketing','Marketing Executive', 45000.00, '2023-04-05', '9876543214');
    
select * from employees;
