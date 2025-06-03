SELECT
player_id
,MIN(event_date) as first_login
FROM Activity
GROUP BY player_id;

-- ROW_NUMBER() solution
-- SELECT player_id, event_date AS first_login
-- FROM (
--     SELECT
--     player_id
--     ,event_date
--     ,ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS rn
--     FROM Activity
-- )
-- WHERE rn = 1;
