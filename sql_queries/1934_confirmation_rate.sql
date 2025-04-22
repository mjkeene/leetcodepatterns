-- If a user_id is not in Confirmations table, then 0
-- Else, ratio of 'confirmed' action / total action
WITH agg AS (
    SELECT s.user_id, c.action
    ,CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END AS action_binary
    FROM Signups s
    LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
)

SELECT
user_id, ROUND(SUM(action_binary) * 1.00 / COUNT(user_id), 2) AS confirmation_rate
FROM agg
GROUP BY user_id
