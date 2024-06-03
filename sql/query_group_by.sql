-- query_group_by.sql

SELECT author_id, COUNT(book_id) as book_count FROM books GROUP BY author_id;
-- Add more group by queries as needed
