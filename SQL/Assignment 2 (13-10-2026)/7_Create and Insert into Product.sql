-- QNO  7: Create and Insert into products Table
-- Columns:

-- product_id INT

-- product_name VARCHAR(100)

-- category VARCHAR(50)

-- price DECIMAL(7,2)

-- stock_quantity INT

-- supplier_name VARCHAR(100)

-- manufacture_date DATE

-- expiry_date DATE

-- Task:

-- Insert 6 products (some with expiry dates, some without)

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(7,2),
    stock_quantity INT,
    supplier_name VARCHAR(100),
    manufacture_date DATE,
    expiry_date DATE
);

INSERT INTO products(product_id, product_name, category, price, stock_quantity,supplier_name, manufacture_date, expiry_date)
	VALUES
    (1, 'Pepsi', 'Beverages', 40.00, 100, 'PepsiCo','2026-01-10', '2026-12-31'),
    (2, 'Notebook', 'Stationery', 60.50, 200, 'Classmate','2026-02-15', NULL),
    (3, 'Milk', 'Dairy', 32.00, 50, 'Amul','2026-10-10', '2026-10-20'),
    (4, 'Shampoo', 'Personal Care', 150.75, 80, 'Dove','2026-03-05', NULL),
    (5, 'Biscuits', 'Food', 25.00, 150, 'Britannia','2026-08-01', '2027-02-01'),
    (6, 'Cooking Oil', 'Grocery', 180.00, 40, 'Fortune','2026-05-20', NULL);
    
select * from products;