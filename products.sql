-- Drop the table if it already exists (optional)
DROP TABLE IF EXISTS products;

-- Create the products table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT
);

-- Insert sample data into the products table
INSERT INTO products (name, price, category, description) VALUES
('Wireless Mouse', 25.99, 'Electronics', 'A sleek wireless mouse with ergonomic design.'),
('Laptop Stand', 49.99, 'Accessories', 'Adjustable aluminum stand for laptops.'),
('Bluetooth Speaker', 89.99, 'Electronics', 'Portable Bluetooth speaker with high-quality sound.'),
('Smartphone', 699.99, 'Electronics', 'Latest 5G-enabled smartphone with 128GB storage.'),
('Office Chair', 199.99, 'Furniture', 'Ergonomic office chair with lumbar support.'),
('Noise Cancelling Headphones', 299.99, 'Electronics', 'Over-ear noise cancelling headphones with Bluetooth.'),
('Mechanical Keyboard', 79.99, 'Accessories', 'Mechanical keyboard with RGB backlighting.'),
('Gaming Mouse Pad', 19.99, 'Accessories', 'Large gaming mouse pad with anti-slip base.'),
('4K Monitor', 399.99, 'Electronics', '27-inch 4K UHD monitor with ultra-thin bezel.'),
('External Hard Drive', 59.99, 'Storage', '1TB external hard drive with USB 3.0.'),
('Wireless Earbuds', 129.99, 'Electronics', 'True wireless earbuds with noise cancellation.'),
('Fitness Tracker', 49.99, 'Wearables', 'Waterproof fitness tracker with heart rate monitoring.'),
('Portable Charger', 39.99, 'Accessories', '10000mAh portable charger with fast charging.'),
('Smartwatch', 199.99, 'Wearables', 'Smartwatch with GPS and heart rate sensor.'),
('Tablet', 299.99, 'Electronics', '10.5-inch tablet with 64GB storage and stylus support.'),
('Electric Kettle', 34.99, 'Appliances', 'Electric kettle with automatic shut-off.'),
('Air Purifier', 149.99, 'Appliances', 'HEPA air purifier with three fan speeds.'),
('Standing Desk', 499.99, 'Furniture', 'Adjustable standing desk with electric height adjustment.'),
('LED Desk Lamp', 29.99, 'Furniture', 'LED desk lamp with adjustable brightness and angle.'),
('Cordless Vacuum', 199.99, 'Appliances', 'Lightweight cordless vacuum cleaner with powerful suction.');
