-- Write only the SQL statement that solves the problem and nothing else.
SELECT name 
FROM employees
WHERE id NOT IN(SELECT managerId FROM employees WHERE managerId IS NOT NULL)
