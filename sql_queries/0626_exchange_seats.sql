CREATE TABLE seat (
    id INT PRIMARY KEY,
    student VARCHAR
);

SELECT 
CASE WHEN id % 2 != 0 AND id + 1 <= (SELECT COUNT(*) FROM Seat) THEN id + 1
     WHEN id % 2 = 0 THEN id - 1
     ELSE id
     END AS id
,student
FROM Seat
ORDER BY id
