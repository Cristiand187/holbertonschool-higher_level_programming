-- lists the number of records with the same score in the table second_table
-- Database hbtn_0c_0 --> arg
SELECT score, COUNT(name) AS number
FROM second_table
GROUP BY score
ORDER BY number desc;
