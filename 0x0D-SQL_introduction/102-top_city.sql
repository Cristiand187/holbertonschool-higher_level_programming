-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Database --> arg; top 3; month --> 7, 8
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
