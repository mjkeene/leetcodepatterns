-- manager IDs with at least 5 direct reports
SELECT name
FROM Employee
WHERE id in (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)

-- WITH manager_ids AS (
--     SELECT managerId, COUNT(DISTINCT id) as num_reports
--     FROM Employee
--     WHERE managerId IS NOT NULL
--     GROUP BY managerId
--     HAVING COUNT(DISTINCT id) >= 5
-- )

-- SELECT e.name
-- FROM Employee e
-- INNER JOIN manager_ids m
-- ON e.id = m.managerId
