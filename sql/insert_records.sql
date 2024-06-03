-- insert_records.sql

-- Insert records into authors table
INSERT INTO authors (author_id, first_name, last_name, year_born) VALUES ('1', 'George', 'Orwell', 1903);
INSERT INTO authors (author_id, first_name, last_name, year_born) VALUES ('2', 'Aldous', 'Huxley', 1894);

-- Insert records into books table
INSERT INTO books (book_id, title, year_published, author_id) VALUES ('1', '1984', 1949, '1');
INSERT INTO books (book_id, title, year_published, author_id) VALUES ('2', 'Brave New World', 1932, '2');
-- Add more records as needed
