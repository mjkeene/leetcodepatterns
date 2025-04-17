SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT
    id
    ,num
    ,LAG(num, 1) OVER(ORDER BY id) as lag_1
    ,LAG(num, 2) OVER(ORDER BY id) as lag_2
    FROM Logs
    )
WHERE num = lag_1 AND num = lag_2;
