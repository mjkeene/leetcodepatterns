-- Order by turn, cumulative sum on weight, then filter for closest value less than
-- or equal to the weight limit without going over -> return their name
SELECT person_name
FROM (
    SELECT person_name, turn, SUM(weight) OVER(ORDER BY turn) AS cumulative_weight
    FROM Queue
    ORDER BY turn DESC
    )
WHERE cumulative_weight <= 1000
LIMIT 1;
