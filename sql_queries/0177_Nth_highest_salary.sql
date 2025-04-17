CREATE OR REPLACE FUNCTION NthHighestSalary(N INT)
RETURNS INT AS $$
    -- Make sure that N value is not negative
    SELECT CASE WHEN N < 1 THEN NULL
    ELSE (
        SELECT DISTINCT e.salary
        FROM Employee e
        ORDER BY salary DESC
        OFFSET N - 1
        LIMIT 1
    )
    END
$$ LANGUAGE SQL;
