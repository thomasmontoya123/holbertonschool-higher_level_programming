-- Creates the table cities.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL ,
    state_id INT NOT NULL ,
    FOREIGN KEY (state_id)
    REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL,
    )  ENGINE=INNODB;