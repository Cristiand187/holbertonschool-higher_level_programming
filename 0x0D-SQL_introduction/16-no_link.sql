-- lists all records of the table second_table of the database hbtn_0c_0
-- Database --> arg; 
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score desc, name desc;
