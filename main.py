from movie_json_parser import MovieJsonParser as MJP

parser = MJP("tmdb_movies.json")
genre_dict = parser.get_genre_dict()
for genre, movie_list in genre_dict.items():
    print("{}: \n************************\n{}\n\n".format(genre, [movie["title"] for movie in movie_list]))