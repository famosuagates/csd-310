-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints/foreign keys if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('4 Privet Drive, Little Whining, Surrey RG129FG');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Philosophers Stone', 'J. K. Rowling', 'It does not do to dwell on dreams and forget to live');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Chamber of Secrets', 'J. K. Rowling', 'Albus Dumbledore is the greatest sorcerer in the world');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Prisoner of Azkaban', 'J. K. Rowling', 'Happiness can be found, even in the darkest of times, if one only remembers to turn on the light');

INSERT INTO book(book_name, author, details)
    VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien', 'It is not despair, for despair is only for those who see the end beyond all doubt. We do not.');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Goblet of Fire', 'J. K. Rowling', 'Dont you turn your back on me, Harry Potter! I want you to look at me when I kill you!');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Order of the Pheonix', 'J. K. Rowling', 'You are a fool, Harry Potter, and you will lose everything');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Half-Blood Prince', 'J. K. Rowling', 'The sixth book, (2005)');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Deathly Hallows', 'J. K. Rowling', 'I must be the one to kill Harry Potter');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Cursed Child', 'J. K. Rowling', 'After all this time? Always!');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Harry', 'Potter');

INSERT INTO user(first_name, last_name)
    VALUES('Tom', 'Riddle');

INSERT INTO user(first_name, last_name)
    VALUES('Severus', 'Snape');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harry'), 
        (SELECT book_id FROM book WHERE book_name = 'The Hobbit or There and Back Again')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Tom'),
        (SELECT book_id FROM book WHERE book_name = 'Harry Potter and the Deathly Hallows')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Severus'),
        (SELECT book_id FROM book WHERE book_name = 'Harry Potter and the Cursed Child')
    );
