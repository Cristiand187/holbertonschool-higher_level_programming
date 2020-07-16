-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (SELECT show_id
    FROM tv_show_genres
    INNER JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy') S
ON tv_shows.id = S.show_id
WHERE S.show_id IS NULL
ORDER BY tv_shows.title
