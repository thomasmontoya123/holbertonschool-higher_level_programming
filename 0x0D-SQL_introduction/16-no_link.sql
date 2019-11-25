-- lists all records of the table avoid NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
