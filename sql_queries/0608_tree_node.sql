-- Root : parent id is null
-- Inner : has a parent id and is a parent id
-- Leaf : has a parent id, but is not a parent id
SELECT id,
CASE WHEN p_id IS NULL THEN 'Root'
    -- Any NOT IN comparison involving a NULL in the subquery evaluates to
    -- UNKNOWN, and the condition fails for all rows, so you must add the WHERE filter.
    -- There will always be a null because of the Root node.
     WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
     ELSE 'Inner'
     END AS type
FROM Tree;
