-- creates the table unique_id
-- id --> 1, UNIQUE
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256));
