-- Query the two cities in STATION with the shortest and longest CITY names,
-- as well as their respective lengths (i.e.: number of characters in the name).
-- If there is more than one smallest or largest city, choose the one that comes
-- first when ordered alphabetically.

SELECT TOP 1 CITY, LEN(CITY) AS city_name_length
FROM STATION
ORDER BY LEN(CITY), CITY

UNION ALL

SELECT TOP 1 CITY, LEN(CITY) AS city_name_length
FROM STATION
ORDER BY LEN(CITY) DESC, CITY

-- MS SQL Server doesn't allow UNION like this, so I had to use CTEs to actually submit it
-- Same idea as above though
WITH shortest_city AS (
    SELECT TOP 1 CITY, LEN(CITY) AS city_name_length
    FROM STATION
    ORDER BY LEN(CITY), CITY
)

,longest_city AS (
    SELECT TOP 1 CITY, LEN(CITY) AS city_name_length
    FROM STATION
    ORDER BY LEN(CITY) DESC, CITY
)

SELECT *
FROM shortest_city

UNION ALL

SELECT *
FROM longest_city
