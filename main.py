from movie_json_parser import MovieJsonParser as MJP

def print_initial_screen():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def print_genres(genre_list):
    print("Available genres: " + ", ".join(genre_list))

def check_input(input_string, check_list): # Checks the string and returns a sublist from the checklist that contain the string
    contain_list = []
    for check in check_list:
        if input_string.lower() in check.lower():
            contain_list.append(check)
    return contain_list

def check_input_loop(check_list): # Loops through until the user has selected a genre
    yes_list = ['y','yes','ye']

    while True:
        current_user_input = get_user_genre_loop(check_list)
        contain_list = check_input(current_user_input, check_list)
        if len(contain_list) > 1:
            print("The following genres contain {}: {}".format(current_user_input, ", ".join(contain_list)))
            print("Did you mean to type one of them?")
        elif len(contain_list) == 1:
            print("Check for {} movies(y/n)?".format(contain_list[0]))
            if str(input()).lower() in yes_list:
                return contain_list[0]
        else:
            print("There were no genres found containing {}. Please try again.".format(current_user_input))

def get_user_genre(genre_list):
    print("Please type a genre, or type 'genres' to see a list of available genres.")
    user_input = input()
    if user_input == 'genres':
        print_genres()
        return None
    else : return str(user_input)

def get_user_genre_loop(genre_list):
    user_input = None
    counter = 0
    while user_input is None:
        user_input = get_user_genre(genre_list)
        counter += 1
        if counter > 10:
            print("An error occured. Please restart the program and try again.")
            return
    return user_input

def get_movie_recommendation(): # main function
    yes_list = ['y','yes','ye']
    parser = MJP("tmdb_movies.json")
    genre_dict = parser.get_genre_dict()
    print_initial_screen()
    go_again = True
    while go_again == True:
        user_genre = check_input_loop(list(genre_dict.keys()))
        print("Check out some of the following movies:")
        for movie in genre_dict[user_genre]:
            print(
                """
                Title: {title}
                Genres: {genres}
                Overview: {overview}
                """.format(
                title = movie["title"],
                genres = movie["genres"],
                overview = movie["overview"]
                )
            )
        print("Begin new search?")
        repeat_input = str(input()).lower()
        if repeat_input not in yes_list:
            go_again = False
    

get_movie_recommendation()