-- Rank the events, and grab the previous login date with LAG()
WITH ranked_player_events AS (
    SELECT player_id, event_date
    ,ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS rn
    ,LAG(event_date, 1) OVER(PARTITION BY player_id ORDER BY event_date) as lagged_date
    FROM Activity
)

-- Case statement identifies "second day logins", which can then be used to count the
-- distinct number of player_ids with those specifications to get the final fraction
,second_day_logins AS (
    SELECT player_id, event_date, lagged_date, rn
    ,CASE WHEN event_date - lagged_date = 1 AND rn = 2 THEN 1 ELSE 0 END AS second_day_login
    FROM ranked_player_events
)

,distinct_player_ids AS (
    SELECT DISTINCT player_id
    FROM Activity
)

SELECT
ROUND(SUM(b.second_day_login) * 1.0 / COUNT(distinct a.player_id), 2) AS fraction
FROM distinct_player_ids a
LEFT JOIN second_day_logins b
ON a.player_id = b.player_id
