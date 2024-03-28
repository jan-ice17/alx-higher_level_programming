-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;