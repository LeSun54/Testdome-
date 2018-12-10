-- Write only the SQL statement that solves the problem and nothing else.
SELECT userId, AVG(duration)
FROM sessions 
GROUP BY userId
HAVING COUNT(userId) > 1
