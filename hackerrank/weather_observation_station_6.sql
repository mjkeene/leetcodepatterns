-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION.
-- Your result cannot contain duplicates.

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY, 1)) IN ('a', 'e', 'i', 'o', 'u');

-- Basic way, pretty repetitive though
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(CITY) LIKE 'a%'
   OR LOWER(CITY) LIKE 'e%'
   OR LOWER(CITY) LIKE 'i%'
   OR LOWER(CITY) LIKE 'o%'
   OR LOWER(CITY) LIKE 'u%';
