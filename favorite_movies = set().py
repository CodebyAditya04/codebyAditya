favorite_movies = set()

while True:
    print("\n--- Favorite Movies Menu ---")
    print("1. Add a movie")
    print("2. Remove a movie")
    print("3. View all movies")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        movie = input("Enter the movie name: ")
        favorite_movies.add(movie.lower())
        print(f"'{movie}' has been added to your favorites.")
    
    elif choice == "2":
        movie = input("Enter the movie to remove: ")
        if movie.lower() in favorite_movies:
            favorite_movies.remove(movie.lower())
            print(f"'{movie}' has been removed.")
        else:
            print(f"'{movie}' is not in your favorites.")
    
    elif choice == "3":
        if not favorite_movies:
            print("You have no favorite movies yet.")
        else:
            print("Your favorite movies are:")
            for m in favorite_movies:
                print(f"- {m.title()}")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Please choose a valid option (1-4).")
