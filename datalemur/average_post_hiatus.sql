-- For each user who posted at least twice in 2021, write a query to find the number of days
-- between each user’s first post of the year and last post of the year in the year 2021.
-- Output the user and number of the days between each user's first and last post.

WITH users_posted_twice_2021 AS (
  SELECT user_id, MIN(post_date) AS min_date, MAX(post_date) AS max_date
  FROM posts
  WHERE EXTRACT(YEAR FROM post_date) = 2021
  GROUP BY 1
  HAVING COUNT(DISTINCT post_id) >= 2
)

SELECT user_id, max_date::date - min_date::date AS days_between
FROM users_posted_twice_2021
