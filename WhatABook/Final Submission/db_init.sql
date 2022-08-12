-- Ryan Long | CYBR410-T301 | 8/12/2022
-- Assuming Database has not been created previously, long_whatabook database will be created
-- If Database was created previously, start with line 9 to select and clear the database then populate fresh sample data

-- create database
CREATE DATABASE long_whatabook;

-- if database exsists, start here
USE long_whatabook;

-- drop/create user with privileges
DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON long_whatabook.* TO'whatabook_user'@'localhost';

-- drop foreign keys and tables
ALTER TABLE wishlist_fields DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist_fields DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store_fields;
DROP TABLE IF EXISTS book_fields;
DROP TABLE IF EXISTS wishlist_fields;
DROP TABLE IF EXISTS user_fields;

-- create tables
CREATE TABLE store_fields (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    time_open   VARCHAR(7)    NOT NULL,
    time_close  VARCHAR(7)    NOT NULL,         
    PRIMARY KEY(store_id)
);

CREATE TABLE book_fields (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user_fields (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist_fields (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book_fields(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user_fields(user_Id)
);

-- populate store
INSERT INTO store_fields(store_id, locale, time_open, time_close) VALUES ('001', '123 A St Omaha, NE 68123', '09:00am', '10:00pm');

-- populate books
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55001', 'The Long Road', 'A store about an orphan and his journey through adoption.', 'Billy Boy');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55002', 'Cooking Part 1', 'Introduction to Cooking.', 'Chef Boyard');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55003', 'Cooking Part 2', 'Advanced Cooking.', 'Chef Boyard');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55004', 'A Dogs Life', 'The adventures of little Mylo.', 'Spot');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55005', 'World Atlas', 'A collection of ancient maps.', 'Kat Ographer');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55006', 'Math for Dummies', 'Introduction to Mathematics.', 'Matt Hard');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55007', 'Bikes are fun', 'Learn how to ride a bicycle.', 'Bak Pedal');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55008', 'Computers 101', 'Introduction to Computers.', 'Bill Gates');
INSERT INTO book_fields(book_id, book_name, details, author) VALUES ('55009', 'Lawns and More', 'A guide to lawn care.', 'Terry Mower');

-- populate users
INSERT INTO user_fields(user_id, first_name, last_name) VALUES ('00001', 'Larry', 'Fine');
INSERT INTO user_fields(user_id, first_name, last_name) VALUES ('00002', 'Curly', 'Howard');
INSERT INTO user_fields(user_id, first_name, last_name) VALUES ('00003', 'Moe', 'Howard');

-- populate wishlist
INSERT INTO wishlist_fields(wishlist_id, user_id, book_id) VALUES ('99001', '00002', '55009');
INSERT INTO wishlist_fields(wishlist_id, user_id, book_id) VALUES ('99002', '00003', '55005');
INSERT INTO wishlist_fields(wishlist_id, user_id, book_id) VALUES ('99003', '00001', '55004');