-- A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
--  It is creating a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Usesthe database just created
USE hbtn_0d_usa
-- Will create a table in the database
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY(id));