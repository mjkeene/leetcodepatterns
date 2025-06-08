CREATE TABLE Cinema (
    id INT PRIMARY KEY,
    movie VARCHAR(100) NOT NULL,
    description VARCHAR(500),
    rating DECIMAL(4, 2) CHECK (rating between 0 and 10)
);

SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 != 0
AND description != 'boring'
ORDER BY rating DESC;
