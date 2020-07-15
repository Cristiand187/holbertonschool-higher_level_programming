-- creates the database hbtn_0d_usa and the table cities
-- cities join states
CREATE DATABASE IF EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) 
    REFERENCES hbtn_0d_usa.states(id));
