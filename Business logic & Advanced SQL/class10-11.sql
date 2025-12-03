CREATE database MOVIE_MANAGMENT;
USE MOVIE_MANAGMENT;

CREATE TABLE MOVIE(
	movie_id INT primary key,
	movie_name VARCHAR(20) not null,
    release_year INT,
    duration decimal(2,2),
    genres VARCHAR(20)
);

CREATE TABLE PRODUCTION(
	production_id INT primary key,
    production_name VARCHAR(20),
    address VARCHAR(20)
);

ALTER TABLE MOVIE
ADD COLUMN production_id INT;


ALTER TABLE MOVIE
ADD CONSTRAINT fk_production
FOREIGN KEY (production_id)
REFERENCES PRODUCTION(production_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
​




