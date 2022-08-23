import sqlite3

from flask import jsonify





def title_info(title_input):

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT `title`, `country`, `release_year`, `listed_in`, `description` from netflix "
                    "ORDER BY date_added DESC ")
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    movie = ""
    #print(result)
    for row in result:
        if title_input == row[0].lower():
            movie += "<pre>"
            movie += f"'title': {row[0]}\n'country': {row[1]}\n'release_year': {row[2]}\n'genre': {row[3]}\n'description': {row[4]}\n\n"
            # movie['title'] = row[0]
            # movie['country'] = row[1]
            # movie['release_year'] = row[2]
            # movie['genre'] = row[3]
            # movie['description'] = row[4]
            break
        else:
            continue
        movie += "</pre>"
    con.close()
    return movie


def year_to_year(beg_year, end_year):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = (f"""SELECT `title`, `release_year` 
                    from netflix 
                    WHERE `release_year` BETWEEN '{beg_year}' AND '{end_year}' 
                    ORDER BY 'release_year' 
                    LIMIT 100 """)

    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    movie_range = []
    #print(result)
    for row in result:
        movie_range.append({'title': row[0], 'release_year': row[1]})

    con.close()
    return movie_range


def movie_by_rating(rating):
    if rating == 'children':
        rating_list = ['G']
    elif rating == 'family':
        rating_list = ['G', 'PG', 'PG-13']
    else:
        rating == 'adult'

        rating_list = ['R', 'NC-17']

    rating = ", ".join([f'"{rating}"' for rating in rating_list])
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = (f"""SELECT `title`, `rating`, `description` 
                    from netflix 
                    WHERE `rating` IN ({rating})
                    ORDER BY 'rating' 
                    LIMIT 100 """)

    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    movie = []
    #print(result)
    for row in result:
        movie.append({'title': row[0], 'rating': row[1], 'description': row[2]})
    con.close()
    return movie


def movie_by_genre(genre):

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = (f"""SELECT `title`, `description` 
                    from netflix 
                    WHERE `listed_in` == '{genre}'
                    ORDER BY 'date_added' DESC 
                    LIMIT 10 """)

    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    movie = []
    #print(result)
    for row in result:
        movie.append({'title': row[0], 'description': row[1]})
    con.close()
    return movie


def two_cast(actor1, actor2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query1 = (f"""SELECT `cast` 
                        from netflix 
                        WHERE `cast` like '%{actor1}%' and `cast` like '%{actor2}%'
                        ORDER BY 'title' 
                        """)
    result1 = cur.execute(sqlite_query1)
    result1 = cur.fetchall()

    con.close()
    cast_list = []
    two_times = []
    for row in result1:
        cast = str(row).strip("(' )")
        cast = cast.strip('"').split(',')
        for item in cast:
            if item in cast_list:
                if item not in two_times:
                    two_times.append(item)
            else:
                if item != '':
                    cast_list.append(item)
    return print(two_times)


# two_cast('Jack Black', 'Dustin Hoffman')


def get_json(movie_type, movie_year, movie_genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = (f"""SELECT `title`, `type`, `release_year`, `listed_in`
                            from netflix 
                            WHERE `listed_in` == '{movie_genre}' 
                            AND `release_year` == '{movie_year}'
                            AND `type` == '{movie_type}'
                            ORDER BY 'title' 
                            """)
    result = cur.execute(sqlite_query)
    result = cur.fetchall()

    movies = []
    # print(result)
    for row in result:
        movies.append({'title': row[0], 'type': row[1], 'release_year': row[2], 'genre': row[3]})
    con.close()
    return jsonify(movies)

print(get_json('Movie', '2017', 'Dramas'))

if __name__ == '__main__':
    title_input = 'man'

