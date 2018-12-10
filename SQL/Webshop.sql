-- Write only the SQL statement that solves the problem and nothing else.
SELECT i.name, s.name
FROM sellers as s
INNER JOIN items as i
ON s.id = i.sellerId
WHERE s.rating > 4
