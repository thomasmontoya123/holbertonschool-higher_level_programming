-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL FOREIGN KEY REFERENCES hbtn_0d_usa.states, name VARCHAR(256));
