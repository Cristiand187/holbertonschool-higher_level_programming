-- script that creates the table id_not_null
-- id --> 1 default
CREATE TABLE IF NOT EXIST id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256));
