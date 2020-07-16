-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
GROUP BY tv_shows.title
ORDER BY tv_shows.title;
