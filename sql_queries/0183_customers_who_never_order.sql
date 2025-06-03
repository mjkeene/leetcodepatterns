SELECT 
c.name AS "Customers"
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
-- could also use o.customerId for NULL check,
-- but best to use primary key in case of schema changes
WHERE o.id IS NULL;
