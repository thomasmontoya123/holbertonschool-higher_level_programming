-- lists the number of records with the same score in the table
SELECT score, count(*) AS number FROM second_table GROUP BY number ORDER DESC;
