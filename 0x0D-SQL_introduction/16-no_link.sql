-- lists all records of table second_table having a name value
-- that records are ordered by descending score.
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC
