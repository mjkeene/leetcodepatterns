-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION.
-- Your result cannot contain duplicates.
-- This is basically identical to problem #6, just ending char instead of beginning

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(RIGHT(CITY, 1)) IN ('a', 'e', 'i', 'o', 'u');

-- Basic / repetitive way again
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(CITY) LIKE '%a'
   OR LOWER(CITY) LIKE '%e'
   OR LOWER(CITY) LIKE '%i'
   OR LOWER(CITY) LIKE '%o'
   OR LOWER(CITY) LIKE '%u';
