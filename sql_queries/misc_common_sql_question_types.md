### Common SQL Question Types

#### 1. DAU / WAU / MAU (Daily/Weekly/Monthly Active Users)
* Find how many users were active on a certain day, week, month.

#### 2. Retention Analysis (Day 1, Day 7, Day 30, etc.)
* What percentage of users came back X days after signup?

#### 3. MoM Growth / Percent Change
* How did active users or engagement change compared to the prior month?

#### 4. User Funnels / Conversion Rates
* Out of users who started a flow (e.g., viewed a post), how many completed next steps (e.g., like, shared)?

#### 5. Feature Adoption
* How many users used a new feature? How many used it more than once?

#### 6. Power Users / Outliers
* Who are the most active users? What percent of users generate 80% of actions?

#### 7. Time to Event / Lag Between Actions
* What's the average time between signup and first post/interaction?

#### 8. Segmentation / Comparison by Group
* What's the DAU by region, platform, age, etc.?

#### Sample SQL Schema for These Question Types

```sql
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    created_at TIMESTAMP,
    region VARCHAR,
    platform VARCHAR,
    age_bucket VARCHAR
);

CREATE TABLE sessions (
    session_id BIGINT PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    session_start TIMESTAMP,
    duration_seconds NUMERIC
);

CREATE TABLE user_events (
    event_id BIGINT PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    event_type VARCHAR,
    event_timestamp TIMESTAMP
)
```

## Example Queries

#### 1. DAU (last 30 days)
```sql
SELECT 
DATE_TRUNC('day', session_start) AS day,
COUNT(DISTINCT user_id) AS dau
FROM sessions
-- use CURRENT_DATE over NOW() for batch jobs like this; NOW() will
-- include time (and will be literally 720 hours from current moment).
-- CURRENT_DATE will be midnight to midnight for exactly 30 full days.
WHERE session_start >= CURRENT_DATE - INTERVAL '30 days'
-- cannot alias column from SELECT in GROUP BY, restate the expression
GROUP BY DATE_TRUNC('day', session_start)
ORDER BY day;
```

#### 2. MAU (last 3 months)
```sql
-- Note that rolling 90 day window is not ideal since you will get 
-- incomplete months, and skew your MAU counts and trends.
-- Not preferred for clear MoM comparisons.
SELECT
DATE_TRUNC('month', session_start) AS month,
COUNT(DISTINCT user_id)
FROM sessions
-- Use this for full calendar months (Apr, May, Jun)
-- DATE_TRUNC('month', CURRENT_DATE) gives you the first day of the
-- current month; subtracting 2 more months gives you start of window.
WHERE session_start >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '2 months'
GROUP BY DATE_TRUNC('month', session_start)
ORDER BY month;
```

#### 3. MoM Growth in MAU
```sql
SELECT
FROM
```
