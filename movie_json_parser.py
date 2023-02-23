import json

class MovieJsonParser:
    def __init__(self, movie_json_file_name) -> None:
        with open(movie_json_file_name, encoding="utf-8") as movies_json:
            self.loaded_movies_json = json.load(movies_json)

    # dict_keys(['budget', 'genres', 'homepage', 'id', 'original_language', 'overview', 'popularity', 
    #   'poster_path', 'release_date', 'revenue', 'runtime', 'tagline', 'title', 'vote_average', 'vote_count', 
    #   'external_ids', 'similar', 'certification', 'directors', 'writers', 'cast', 'trailer_yt'])
    
    def get_genres_list(self): # returns a list of all unique genres from the movies
        genre_list = []

        for movie in self.loaded_movies_json:
            genres = movie["genres"]
            if type(genres) == str: genres = [genres]
            for genre in genres:
                if genre not in genre_list: genre_list.append(genre)
        genre_list.sort()
        return genre_list
    

    def get_genre_dict(self): # returns a dictionary of genres holding links to all the appropriate movies
        genre_dict = {genre:[] for genre in self.get_genres_list()}
        for movie in self.loaded_movies_json:
            genres = movie["genres"]
            if type(genres) == str: genres = [genres]
            for genre in genres:
                genre_dict[genre].append(movie)
        return genre_dict
