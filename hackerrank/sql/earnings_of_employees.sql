-- Simpler without CTE
-- Note that you cannot reference column aliases from SELECT in HAVING or GROUP BY
SELECT months * salary AS earnings, COUNT(employee_id)
FROM Employee
GROUP BY months * salary
HAVING months * salary = (SELECT MAX(months * salary) FROM Employee);
--
--WITH total_earnings AS (
--    SELECT employee_id, name, months, salary, months * salary AS earnings
--    FROM Employee
--)
--
--SELECT earnings, COUNT(employee_id) AS num_employees
--FROM total_earnings
--WHERE earnings = (SELECT MAX(earnings) FROM total_earnings)
--GROUP BY earnings;
