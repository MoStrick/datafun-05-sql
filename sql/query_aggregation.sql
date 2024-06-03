-- query_aggregation.sql

SELECT author_id, COUNT(book_id) as book_count FROM books GROUP BY author_id;
SELECT AVG(year_published) as average_year FROM books;
-- Add more aggregations as needed
