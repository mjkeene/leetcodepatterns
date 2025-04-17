-- Wrap subquery to return NULL if no result
SELECT (
    SELECT DISTINCT e.salary
    FROM Employee e
    ORDER BY e.salary DESC
    -- Skip 1 row
    OFFSET 1
    -- Return only 1 row (second row since we skip the first)
    LIMIT 1
) AS "SecondHighestSalary";
