-- lists all cities contained in the database hbtn_0d_usa
SELECT S.*, C.name
FROM states S
INNER JOIN cities C
on S.id = C.state_id
