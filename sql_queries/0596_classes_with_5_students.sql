CREATE TABLE Courses (
    student VARCHAR NOT NULL,
    class VARCHAR NOT NULL,
    PRIMARY KEY (student, class)
);

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
