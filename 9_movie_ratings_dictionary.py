def main():
  
    movie_ratings = {'Interstellar': 10, 'Inception': 9, 'Barbie': 8, 'Doctor Strange In The Multiverse of Madness': 4, 'Son Of The Mask': 0}

    movie_title = input('Enter a movie title: ').title()
    print()

    recommend_movie(movie_ratings, movie_title)

def recommend_movie(movie_ratings, movie_title):
    if movie_title in movie_ratings:
        if movie_ratings[movie_title] >= 8:
            print(f"{movie_title} is rated {movie_ratings[movie_title]}/10. I think you should check it out!")
            print()
        else:
            print(f"You entered {movie_title} which is rated lower than 8/10. Check out some of these other highly rated movies:")
            for title, rating in movie_ratings.items():
                if rating >= 8:
                    print()
                    print(f"    Movie Title: {title:<15} Rated: {rating}/10")
                    print()
    else:
        print(f"You entered {movie_title} which is not found in our catalogue. Check out some of these other highly rated movies:")
        for title, rating in movie_ratings.items():
                if rating >= 8:
                    print()
                    print(f"    Movie Title: {title:<15} Rated: {rating}/10")
                    print()

main()