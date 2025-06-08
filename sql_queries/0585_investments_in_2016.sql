CREATE TABLE insurance (
    pid INT PRIMARY KEY,
    tiv_2015 FLOAT NOT NULL,
    tiv_2016 FLOAT NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL
);

SELECT ROUND(SUM(tiv_2016)::NUMERIC, 2) as tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) >= 2
    )
AND (lat, lon) NOT IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) >= 2
)
