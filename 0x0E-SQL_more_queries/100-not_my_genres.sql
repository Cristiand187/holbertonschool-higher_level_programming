-- database dump from hbtn_0d_tvshows
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT genre_id 
    FROM tv_show_genres
    INNER JOIN tv_shows 
    ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter') G
ON G.genre_id = tv_genres.id
WHERE G.genre_id IS NULL
GROUP BY tv_genres.name;
