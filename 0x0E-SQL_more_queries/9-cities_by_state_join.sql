-- lists all cities contained in the database hbtn_0d_usa
SELECT C.*, S.name
FROM states S
INNER JOIN cities C
on S.id = C.state_id
