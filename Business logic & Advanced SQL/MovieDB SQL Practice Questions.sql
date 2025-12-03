-- MOVIE DATABASE SCHEMA --
CREATE DATABASE MovieDB;
USE MovieDB;

-- 1. PRODUCTION_COMPANY --
CREATE TABLE ProductionCompany (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255)
);

-- 2. PERSON (includes both actors and directors)--
CREATE TABLE Person (
    PersonID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    DateOfBirth DATE
);

-- 3. MOVIE --
CREATE TABLE MOVIE (
MOVIE_ID INT AUTO_INCREMENT PRIMARY KEY,
MOVIE_NAME VARCHAR(25) NOT NULL,
YEAR_D YEAR NOT NULL,
LENGTH INT,
PLOTOUTLINE TEXT,
CompanyID INT,
CONSTRAINT FK_MOVIE_COMPANY
	FOREIGN KEY (CompanyID)
    REFERENCES ProductionCompany(CompanyID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- 4. GENER --
CREATE TABLE GENER (
GENER_ID INT AUTO_INCREMENT PRIMARY KEY,
GENER_NAME VARCHAR(25) UNIQUE
);

-- 5. MOVEI GENER --
CREATE TABLE MOVIE_GENER (
MOVIE_ID INT,
CONSTRAINT FK_MOVIE_GENER
	FOREIGN KEY (MOVIE_ID)
    REFERENCES MOVIE(MOVIE_ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
GENER_ID INT,
CONSTRAINT FK_GENER_ID
	FOREIGN KEY (GENER_ID)
    REFERENCES GENER(GENER_ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
-- 6. MOVEI PERSON --
CREATE TABLE MOVIE_PERSON (
MOVIE_ID INT,
CONSTRAINT FK_MOVIE_ID
	FOREIGN KEY (MOVIE_ID)
    REFERENCES MOVIE(MOVIE_ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
PERSON_ID INT,
CONSTRAINT FK_PERSON_ID
	FOREIGN KEY (PERSON_ID)
    REFERENCES person(PersonID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
ROLE_TYPE VARCHAR(25),
CHARA_NAME VARCHAR(25)
);

-- 7. QUATE --
CREATE TABLE QUOTE (
QUOTE_ID INT AUTO_INCREMENT PRIMARY KEY,
QUOTE_TEXT TEXT,
MOVIE_ID INT,
CONSTRAINT FK_QUOTE_MOVIE
	FOREIGN KEY (MOVIE_ID)
    REFERENCES MOVIE(MOVIE_ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
PERSON_ID INT,
CONSTRAINT FK_QUOTE_PERSON
	FOREIGN KEY (PERSON_ID)
    REFERENCES person(PersonID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- PRODUCTIONCOMPANY
INSERT INTO PRODUCTIONCOMPANY(NAME,ADDRESS)
VALUES("DREAM WORK","USA"),
("WANER BROS","CALIFORNIA"),
("BROS","Oman"),
('DreamWorks', 'Hollywood Blvd'),
('Warner Bros', 'Burbank'),
('Universal Pictures', 'Los Angeles'),
('Indie Films', 'Unknown Street');

-- PERSON
INSERT INTO PERSON (NAME,DATEOFBIRTH)
VALUES('Christopher Nolan', '1970-07-30'),
       ('Leonardo DiCaprio', '1974-11-11'),
       ('Joseph Gordon-Levitt', '1981-02-17'),
       ('Elliot Page', '1987-02-21'),
       ('Quentin Tarantino', '1963-03-27'),
       ('Samuel L. Jackson', '1948-12-21'),
       ('Matt Damon', '1970-10-08'),
       ('Ridley Scott', '1937-11-30');
       
-- MOVIE
INSERT INTO MOVIE (MOVIE_NAME,YEAR_D,LENGTH,PLOTOUTLINE,CompanyID)
VALUES('Inception', 2010, 148,'A thief enters dreams to steal secrets.',1),
       ('Pulp Fiction', 1994, 154,'The lives of criminals intertwine in Los Angeles.',2),
       ('The Martian', 2015, 144, 'An astronaut stranded on Mars must survive.', 3),
('Indie Dreams', 2022, 120, 'An independent film with low budget.', NULL);
       
-- Genres
INSERT INTO GENER (Gener_Name)
VALUES ('Science Fiction'),
	('Crime'),
	('Drama'),
	('Comedy'),
	('Adventure');


-- Link Movies with Genres
INSERT INTO Movie_Gener (Movie_ID, Gener_ID)
VALUES (1, 1), -- Inception -> Science Fiction
      (1, 5),  -- Inception → Adventure
      (2, 2),  -- Pulp Fiction → Crime
      (3, 1),  -- The Martian → Science Fiction
      (3, 3);  -- The Martian → Drama
       
-- Movie_Person (Roles)
-- Inception: Nolan (Director), Leonardo, Joseph, Elliot (Actors)
INSERT INTO Movie_Person (Movie_ID, Person_ID, Role_Type, Chara_Name)
VALUES (1, 1, 'Director', NULL),
       (1, 2, 'Actor', 'Cobb'),
       (1, 3, 'Actor', 'Arthur'),
       (1, 4, 'Actor', 'Ariadne');

-- Pulp Fiction: Tarantino (Director + Actor)
INSERT INTO Movie_Person (Movie_ID, Person_ID, Role_Type, Chara_Name)
VALUES (2, 5, 'Director', NULL),
       (2, 5, 'Actor', 'Jimmie Dimmick'),
       (3, 8, 'Director', NULL),
(3, 7, 'Actor', 'Mark Watney');

-- Quotes
INSERT INTO Quote (Quote_Text, Movie_ID, Person_ID)
VALUES ('You mustn’t be afraid to dream a little bigger, darling.', 1, 2),
       ('Just because you are a character doesn’t mean you have character.', 2, 5),
       ('Just because you are a character doesn’t mean you have character.', 2, 6),
('I’m going to have to science the hell out of this.', 3, 7);


-- QQ  SELECTION QUERIES (SELECT / WHERE / LIKE / IN):
-- 1. isplay all movies from the `Movie` table:
select * from movie;

 -- 2. Show only the `Title` and `Year` of each movie.
 select MOVIE_NAME , YEAR_D from movie;

-- 3. Find all movies released after the year **2000**
select * from movie WHERE YEAR_D>2000;

-- 4. Display all persons born after **1980**
SELECT * FROM Person WHERE DateOfBirth >= '1981-01-01';

-- 5. List all movies that are longer than **140 minutes**
select*from movie where LENGTH>140;

-- 6. Show the name and address of all production companies
SELECT Name, Address FROM ProductionCompany;

-- 7. Find all people whose names start with the letter **'C'**
SELECT *FROM PERSON WHERE Name LIKE 'C%';

-- 8. Show all genres that contain the word **“Drama”**
SELECT *FROM GENER WHERE GENER_NAME LIKE '%Drama%';

-- 9. Display movies produced by **Warner Bros** only
SELECT m.* FROM MOVIE AS m
JOIN ProductionCompany AS pc
  ON m.CompanyID = pc.CompanyID
WHERE pc.Name IN ('WANER BROS', 'Warner Bros');
-- Alternative (more flexible):
-- WHERE pc.Name LIKE '%Warner%';

-- 10. List all persons whose names are **either** 'Leonardo DiCaprio', 'Elliot Page', or 'Matt Damon'
SELECT *FROM PERSON WHERE Name IN ('Leonardo DiCaprio', 'Elliot Page', 'Matt Damon');

--  QQ UPDATE QUERIES:
-- 1. Update the address of **DreamWorks** to `'Hollywood, Los Angeles'`:
UPDATE ProductionCompany SET Address = 'Hollywood, Los Angeles' WHERE Name = 'DreamWorks';

-- 2. Change the `Length` of the movie **“Inception”** to **150** minutes:
UPDATE movie set LENGTH =150 where MOVIE_NAME='Inception';

-- 3. Update the `PlotOutline` of **“The Martian”** to `'Updated for survival mission.'`.
UPDATE MOVIE SET PLOTOUTLINE = 'Updated for survival mission.' WHERE MOVIE_NAME = 'The Martian';

-- 4. Change the production company of **“Indie Dreams”** to be **Indie Films**.
SELECT CompanyID FROM ProductionCompany WHERE Name = 'Indie Films';
UPDATE MOVIE SET CompanyID = 7 WHERE MOVIE_NAME = 'Indie Dreams';

-- 5. Update **Elliot Page’s** birth date to `'1987-03-01'`:
UPDATE PERSON SET DateOfBirth = '1987-03-01' WHERE Name = 'Elliot Page';

-- QQ DELETE QUERIES:
-- 1. Delete the movie named **“Indie Dreams”**:
DELETE from MOVIE where MOVIE_NAME='Indie Dreams';

-- 2. Delete any genre called **“Comedy”** (if it exists):
DELETE FROM GENER WHERE GENER_NAME = 'Comedy';

-- 3. Delete the person **“Matt Damon”** from the database:
DELETE FROM PERSON WHERE Name = 'Matt Damon';

-- 4. Remove all quotes related to **MovieID = 3 (The Martian)**:
DELETE FROM QUOTE WHERE MOVIE_ID = 3;

-- QQ  INSERT QUERIES:
-- 1. Insert a new production company named **“Pixar Animation Studios”** with address `'Emeryville, California'`:
INSERT INTO ProductionCompany (Name, Address)
VALUES ('Pixar Animation Studios', 'Emeryville, California');

-- 2. Insert a new movie **“Toy Story”** (Year: 1995, Length: 81, Company: Pixar):
SELECT CompanyID FROM ProductionCompany WHERE Name = 'Pixar Animation Studios';  -- is 8

INSERT INTO MOVIE (MOVIE_NAME, YEAR_D, LENGTH, PLOTOUTLINE, CompanyID)
VALUES ('Toy Story', 1995, 81, 'Animated story about toys coming to life.', 8);

-- 3. Add a new person **Tom Hanks** (Date of Birth: `'1956-07-09'`)
INSERT INTO PERSON (Name, DateOfBirth)
VALUES ('Tom Hanks', '1956-07-09');

-- 4. Assign **Tom Hanks** as an actor in **Toy Story**, character `'Woody'`.
SELECT MOVIE_ID FROM MOVIE WHERE MOVIE_NAME = 'Toy Story';  -- 5
SELECT PersonID FROM PERSON WHERE Name = 'Tom Hanks'; -- 9

INSERT INTO MOVIE_PERSON (MOVIE_ID, PERSON_ID, ROLE_TYPE, CHARA_NAME)
VALUES (5, 9, 'Actor', 'Woody');

-- 5. Insert a new quote: `'To infinity and beyond!'` spoken by **Tom Hanks** in **Toy Story**.
INSERT INTO QUOTE (QUOTE_TEXT, MOVIE_ID, PERSON_ID)
VALUES ('To infinity and beyond!', 5, 9);

-- JOIN QUERIES (INNER, LEFT, RIGHT)
-- QQ INNER JOIN:
-- 1. Show all **movies** with their **genres**:
SELECT 
    M.MOVIE_NAME AS Movie,
    G.GENER_NAME AS Genre
FROM MOVIE AS M
INNER JOIN MOVIE_GENER AS MG 
    ON M.MOVIE_ID = MG.MOVIE_ID
INNER JOIN GENER AS G 
    ON MG.GENER_ID = G.GENER_ID;

-- 2. Show all **movies** with their **directors**.
SELECT 
    M.MOVIE_NAME Movie,
    P.Name Director
FROM MOVIE M
INNER JOIN MOVIE_PERSON MP 
    ON M.MOVIE_ID = MP.MOVIE_ID
INNER JOIN PERSON P 
    ON MP.PERSON_ID = P.PersonID
WHERE MP.ROLE_TYPE = 'Director';

-- 3. Display all **actors** and the **movies** they acted in:
SELECT 
    P.Name Actor,
    M.MOVIE_NAME Movie,
    MP.CHARA_NAME Character_Name
FROM PERSON P
INNER JOIN MOVIE_PERSON MP 
    ON P.PersonID = MP.PERSON_ID
INNER JOIN MOVIE M 
    ON MP.MOVIE_ID = M.MOVIE_ID
WHERE MP.ROLE_TYPE = 'Actor';

-- 4. Show each **quote**, along with the **movie title** and the **speaker’s name**.
SELECT 
    Q.QUOTE_TEXT Quote,
    M.MOVIE_NAME Movie,
    P.Name Speaker
FROM QUOTE Q
INNER JOIN MOVIE M ON Q.MOVIE_ID = M.MOVIE_ID
INNER JOIN PERSON P ON Q.PERSON_ID = P.PersonID;

-- LEFT JOIN
-- 5. List all **movies** with their **genres** (even movies without a genre).
SELECT 
    M.MOVIE_NAME Movie,
    G.GENER_NAME Genre
FROM MOVIE M
LEFT JOIN MOVIE_GENER MG ON M.MOVIE_ID = MG.MOVIE_ID
LEFT JOIN GENER G ON MG.GENER_ID = G.GENER_ID;

-- 6. List all **movies** with their **production company names**, even if some movies don’t have one.
SELECT 
    M.MOVIE_NAME Movie,
    PC.Name Production_Company
FROM MOVIE M
LEFT JOIN ProductionCompany PC ON M.CompanyID = PC.CompanyID;

-- 7. List all **movies** with their **actors** (show NULL if no actor yet).
SELECT 
    M.MOVIE_NAME Movie,
    P.Name Actor,
    MP.CHARA_NAME Character_Name
FROM MOVIE M
LEFT JOIN MOVIE_PERSON MP ON M.MOVIE_ID = MP.MOVIE_ID AND MP.ROLE_TYPE = 'Actor'
LEFT JOIN PERSON P ON MP.PERSON_ID = P.PersonID;

--  RIGHT JOIN
-- 8. Show all **genres** and the **movies** that belong to them (even if no movie uses that genre).
SELECT 
    M.MOVIE_NAME Movie,
    G.GENER_NAME Genre
FROM MOVIE M
RIGHT JOIN MOVIE_GENER MG ON M.MOVIE_ID = MG.MOVIE_ID
RIGHT JOIN GENER G ON MG.GENER_ID = G.GENER_ID;

-- 9. Show all **production companies** and any **movies** they have produced (even if some companies have none).
SELECT 
    M.MOVIE_NAME Movie,
    PC.Name Production_Company
FROM MOVIE M
RIGHT JOIN ProductionCompany PC ON M.CompanyID = PC.CompanyID;
