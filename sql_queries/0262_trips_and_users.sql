-- Write your PostgreSQL query statement below
SELECT request_at AS "Day",
ROUND(SUM(CASE WHEN status LIKE '%cancelled%' THEN 1 ELSE 0 END) * 1.0 / COUNT(id), 2) AS "Cancellation Rate"
FROM (
    SELECT a.*
    ,b.banned AS client_banned
    ,c.banned AS driver_banned
    FROM Trips a
    LEFT JOIN Users b ON a.client_id = b.users_id
    LEFT JOIN Users c ON a.driver_id = c.users_id
)
WHERE client_banned = 'No' and driver_banned = 'No'
AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 1
