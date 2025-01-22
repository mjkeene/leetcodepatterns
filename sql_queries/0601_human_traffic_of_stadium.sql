-- Write your PostgreSQL query statement below
WITH ranked_stadium AS (
    SELECT s.*
    ,LAG(people, 1) OVER(ORDER BY visit_date) AS lag_1
    ,LAG(people, 2) OVER(ORDER BY visit_date) AS lag_2
    ,LEAD(people, 1) OVER(ORDER BY visit_date) AS lead_1
    ,LEAD(people, 2) OVER(ORDER BY visit_date) AS lead_2
    FROM Stadium s
)

,filtered_stadium AS (
SELECT r.*
,CASE WHEN (people >= 100 AND lag_1 >= 100 AND lag_2 >= 100) OR
           (people >= 100 AND lead_1 >= 100 AND lead_2 >= 100) OR
           (people >= 100 AND lag_1 >= 100 AND lead_1 >= 100)
           THEN 1 ELSE 0 END AS flag
FROM ranked_stadium r
)

SELECT id, visit_date, people
FROM filtered_stadium
WHERE flag = 1
