-- Write an SQL query to list the names of the top three longest osngs by descending order of length

SELECT name FROM songs
ORDER BY duration_ms
DESC LIMIT 5;
